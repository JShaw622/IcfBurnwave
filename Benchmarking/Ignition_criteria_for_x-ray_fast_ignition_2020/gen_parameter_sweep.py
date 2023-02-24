# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:04:55 2023

@author: Jack Shaw

NOTE: Improvement can be made by having separate PATH and filenames
"""

original_f = "test.inf"
#print(original_f.read())


def get_filenames(n_temp=10, n_radius=10, PATH="scripts/"):
    f = []
    filenames =[]
    #this will create the files if needed
    for i in range(n_temp):
        for j in range(n_radius):
            filename = "test_" + str(i)+"_"+str(j)+".inf"
            filenames.append(filename)
        
            print("Making file: " +PATH+ filename)
            f.append(open(PATH+filename,"w"))
    return filenames

#opens the files and copies orignal file contents to them but changes the first line to the name of the file
def init_files(names, original_filename, PATH="scripts/"):
    o_f = open(original_filename, "r").readlines()
    for n in names:
        print("Initialising file: " + PATH+n)
        f = open(PATH+n, "w")
        o_f[0] = n[0:-4]+"\n"
        f.writelines(o_f)
        f.close()
    
#loops through files and changes the temperature of the hotspot between init_T and final_T
def T_sweep(names, init_T = 1, final_T = 1, n_Temps=10, n_radius=10, PATH="scripts/"):
    steps = n_Temps-1
    T = init_T
    T_increment =(final_T-init_T)/steps
    c=0
    for i in range(0, len(names), n_radius):
        for j in range(n_radius):
            o_f = open(PATH+names[c], "r").readlines()
            print("T sweep file: " +PATH+ names[c])
            f = open(str(PATH)+str(names[c]), "w")
            o_f[11] = "DEFINE HsTemp "+str(round(T,2))+"\n"
            f.writelines(o_f)
            f.close()
            c+=1
        T+=T_increment
#sweeps through radius between init_r and final_r
def r_sweep_radius(names, init_r = 0.001, final_r=0.01,n_Temps=10, n_radius=10,PATH="scripts/"):
    steps = n_radius-1
    r = init_r
    r_increment =(final_r-init_r)/steps

    
    i=0
    for n in names:
        if i >=n_radius:
            r=init_r
            i=0
        i+=1    
        o_f = open(PATH+n, "r").readlines()
        #print("Radius sweep file: " + n)
        f = open(PATH+n, "w")
        o_f[6] = "DEFINE HsRad "+str(round(r,5))+"\n"
        r+=r_increment
        f.writelines(o_f)
        f.close()

#generates a list of the names of output files to be read by dataprocessing    
def gen_cdf_list(filenames, PATH="data/"):
    f= open("inputFiles.txt", "w")
    
    for n in filenames:
        f.writelines(PATH+n[0:-3]+"cdf\n")

#generates the batch file for scarf to run
def gen_scarf_batch_file(filenames,PATH="/home/vol05/scarf1185/icfBurnwave/test/scripts/", scripts_per_file=10):
    print("Creating batch file")
    
    f = (open("batchfiles/runScripts.sh", "w", newline="\n"))
    
    #Parameters 
    f.writelines("#!/bin/bash\n")
    f.writelines("#SBATCH --job-name=Hyburn\n")
    f.writelines("#SBATCH -p scarf\n")
    f.writelines("#SBATCH --output=hyades_output.txt\n")
    f.writelines("#SBATCH --ntasks=20\n")
    f.writelines("#SBATCH --cpus-per-task=1\n")
    f.writelines("#SBATCH --time=23:59:59\n")
#Commands for runing scripts
    for n in filenames:
        f.writelines("hyades -c "+PATH+n+"\n")
    #Commands for converting to cdf file
    for n in filenames:
        f.writelines("ppf2ncdf "+PATH+n[0:-3]+"ppf\n")
    f.close()
    
    
filePATH = "scripts/radTransportOn/fluxLimit/"
no_tempSweeps = 5
no_radiusSweeps = 20

filenames = get_filenames(no_tempSweeps, no_radiusSweeps, PATH = filePATH)

init_files(filenames, original_f,PATH = filePATH)

T_sweep(filenames, 5, 20, n_Temps=no_tempSweeps, n_radius=no_radiusSweeps,PATH = filePATH)
r_sweep_radius(filenames, init_r = 0.003, final_r=0.006, n_Temps=no_tempSweeps, n_radius=no_radiusSweeps,PATH = filePATH)

gen_scarf_batch_file(filenames)
gen_cdf_list(filenames, PATH = "data/radTransportOn/fluxLimit/")