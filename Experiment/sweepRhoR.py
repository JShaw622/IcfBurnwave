# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:42:27 2023

@author: Jack Shaw

This is to generate a parameter sweep chainging the radius of the barrier for a
 set density and changing the radius of the hotspot to find ignition point.
"""

original_f = "data/radiusSweep10KeVColdBarrierWide/originalInput.inf"

#creates a list of filenames and creates the files
def get_filenames(T, n_Hs_radius=10, n_barrier_radius=10, PATH="data/"):
    f = []
    filenames =[]
    #this will create the files if needed
    for i in range(n_Hs_radius):
        for j in range(n_barrier_radius):
            filename = "test_T_"+ str(T)+ "_" + str(i)+"_"+str(j)+".inf"
            filenames.append(filename)
        
            print("Making file: " +PATH+ filename)
            f=open(PATH+filename,"w")
            f.close()
    return filenames

#opens the files and copies orignal file contents to them but changes the first line to the name of the file
def init_files(names, original_filename, PATH="data/"):
    o_f = open(original_filename, "r").readlines()
    for n in names:
        print("Initialising file: " + PATH+n)
        f = open(PATH+n, "w")
        o_f[0] = n[0:-4]+"\n"
        f.writelines(o_f)
        f.close()
        
#sweeps through radius between init_r and final_r
def r_sweep_Hs_radius(names, init_r = 0.001, final_r=0.01, n_Hs_radius=10, PATH="data/"):
    r = init_r
    r_increment =(final_r-init_r)/(n_Hs_radius-1)
    i=0
    
    for n in names:
        if i >=n_Hs_radius:
            r=init_r
            i=0
        i+=1    
        o_f = open(PATH+n, "r").readlines()
        #print("Radius sweep file: " + n)
        f = open(PATH+n, "w")
        o_f[6] = "DEFINE HsRad "+str("%.5f" % round(r,5))+"\n"
        r+=r_increment
        f.writelines(o_f)
        f.close()
        
#loops through files and changes the temperature of the hotspot between init_r and final_r
def r_sweep_barrier_radius(names, init_r = 0.001, final_r=0.01, n_Hs_radius=10, n_barrier_radius=10, PATH="data/"):
    steps = n_barrier_radius-1
    r = init_r
    r_increment =(final_r-init_r)/steps
    c=0
    for i in range(0, len(names), n_Hs_radius):
        for j in range(n_Hs_radius):
            print(j, i/n_Hs_radius, r)
            o_f = open(PATH+names[c], "r").readlines()
            #print("Barrier radius sweep file: " +PATH+ names[c])
            f = open(str(PATH)+str(names[c]), "w")
            #Read find the current hotspot radius
            HsRad = float((o_f[6])[-7:-1])
            o_f[13] = "DEFINE BendRad "+str("%.5f" % round(HsRad+r,5))+"\n"
            f.writelines(o_f)
            f.close()
            c+=1
        r+=r_increment
        
#generates a list of the names of output files to be read by dataprocessing    
def gen_cdf_list(filenames, PATH="data/"):
    f= open(PATH+"inputFiles.txt", "w")
    
    for n in filenames:
        f.writelines(PATH+n[0:-3]+"cdf\n")

#generates the batch file for scarf to run
def gen_scarf_batch_file(filenames,localPATH="batchfiles/", scarfPATH="/home/vol05/scarf1185/icfBurnwave/test/coldWide/"):
    #Finding number of tasks
    n_tasks = len(filenames)*2
    
    print("Creating batch file")
    
    f = (open(localPATH+ "runScriptsColdBarrierWide.sh", "w", newline="\n"))
    
    #Parameters 
    f.writelines("#!/bin/bash\n")
    f.writelines("#SBATCH --job-name=Hyburn2\n")
    f.writelines("#SBATCH -p scarf\n")
    f.writelines("#SBATCH --output=hyades_output.txt\n")
    f.writelines("#SBATCH --ntasks="+str(n_tasks)+"\n")
    f.writelines("#SBATCH --cpus-per-task=1\n")
    f.writelines("#SBATCH --time=23:59:59\n")
#Commands for runing scripts
    for n in filenames:
        f.writelines("hyades -c "+scarfPATH+n+"\n")
        #Commands for converting to cdf file
        f.writelines("ppf2ncdf "+scarfPATH+n[0:-3]+"ppf\n")
    f.close()

filePATH = "data/radiusSweep10KeVColdBarrierWide/"
no_barrierRadSweeps = 2
no_radiusSweeps = 5

filenames = get_filenames(10,n_Hs_radius=no_radiusSweeps,n_barrier_radius=no_barrierRadSweeps, PATH = filePATH)

init_files(filenames, original_f,PATH = filePATH)

r_sweep_Hs_radius(filenames, init_r = 0.006, final_r=0.011, n_Hs_radius=no_radiusSweeps,PATH = filePATH)
r_sweep_barrier_radius(filenames, init_r=0.00001, final_r=0.0003, n_Hs_radius=no_radiusSweeps, n_barrier_radius=no_barrierRadSweeps, PATH=filePATH)

gen_scarf_batch_file(filenames)
gen_cdf_list(filenames, PATH = filePATH)