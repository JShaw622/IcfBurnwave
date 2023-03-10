# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:36:07 2023

@author: Jack Shaw
"""

original_f = "data/convergenceTest/originalInput.inf"

#creates a list of filenames and creates the files
def get_filenames(steps, PATH="data/"):
    f = []
    filenames =[]
    #this will create the files if needed
    for i in range(steps):
        filename = "test_"+str(i)+".inf"
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
    
def genSweep(names, steps, originalF, startGroups=5, finalGroups=155, PATH="data/"):
    initNo = startGroups
    groupIncriment =(finalGroups-startGroups)/(steps-1)
    i=0
    group=initNo
    for n in names:
        if i >=steps:
            group=initNo
            i=0
        i+=1    
        o_f = open(PATH+n, "r").readlines()
        #print("Radius sweep file: " + n)
        f = open(PATH+n, "w")
        o_f[51] = "GROUP 1 "+str(group)+"0.001 100\n"
        group+=groupIncriment
        f.writelines(o_f)
        f.close()
        
#generates a list of the names of output files to be read by dataprocessing    
def gen_cdf_list(filenames, PATH="data/"):
    f= open(PATH+"inputFiles.txt", "w")
    
    for n in filenames:
        f.writelines(PATH+n[0:-3]+"cdf\n")

#generates the batch file for scarf to run
def gen_scarf_batch_file(filenames,localPATH="batchfiles/", scarfPATH="/home/vol05/scarf1185/icfBurnwave/test/scipts/Convergence/"):
    #Finding number of tasks
    n_tasks = len(filenames)*2
    
    print("Creating batch file")
    
    f = (open(localPATH+ "runScriptsConvergence.sh", "w", newline="\n"))
    
    #Parameters 
    f.writelines("#!/bin/bash\n")
    f.writelines("#SBATCH --job-name=HyburnConvergence\n")
    f.writelines("#SBATCH -p scarf\n")
    f.writelines("#SBATCH --output=hyades_outputConvergence.txt\n")
    f.writelines("#SBATCH --ntasks="+str(n_tasks)+"\n")
    f.writelines("#SBATCH --cpus-per-task=1\n")
    f.writelines("#SBATCH --time=23:59:59\n")
#Commands for runing scripts
    for n in filenames:
        f.writelines("hyades -c "+scarfPATH+n+"\n")
        #Commands for converting to cdf file
        f.writelines("ppf2ncdf "+scarfPATH+n[0:-3]+"ppf\n")
    f.close()

filePATH = "data/convergenceTest/"
no_groupSteps = 5

filenames = get_filenames(no_groupSteps, PATH = filePATH)

init_files(filenames, original_f,PATH = filePATH)
genSweep(filenames,no_groupSteps,original_f, PATH=filePATH)

gen_scarf_batch_file(filenames)
gen_cdf_list(filenames, PATH = filePATH)
