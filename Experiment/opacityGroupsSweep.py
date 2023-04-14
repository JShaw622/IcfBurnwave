# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:36:07 2023

@author: Jack Shaw
"""

original_f = "data/opacityConvergence/originalInput.inf"

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
    
def genSweep(names, steps, originalF, startGroups=50, finalGroups=2000, PATH="data/"):
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
        o_f[51] = "GROUP 1 150 1 "+str(round(group))+"\n"
        group+=groupIncriment
        f.writelines(o_f)
        f.close()
        
#generates a list of the names of output files to be read by dataprocessing    
def gen_cdf_list(filenames, PATH="data/"):
    f= open(PATH+"inputFiles.txt", "w")
    
    for n in filenames:
        f.writelines(PATH+n[0:-3]+"cdf\n")

#generates the batch file for scarf to run
def gen_scarf_batch_file(filenames,localPATH="batchfiles/", scarfPATH="/home/vol05/scarf1185/icfBurnwave/test/scripts/Convergence/"):
    #Finding number of tasks
    #Finding number of tasks
    n_tasks = len(filenames)
    
    print("Creating batch files")
    
    f = (open(localPATH+ "runScriptsConvergence.sh", "w", newline="\n"))
    f2 = (open(localPATH+ "convertBatch.sh", "w", newline="\n"))
    
    #Parameters 
    f.writelines("#!/bin/bash\n")
    f.writelines("#SBATCH --job-name=HyburnConvergence\n")
    f.writelines("#SBATCH -p scarf\n")
    f.writelines("#SBATCH --output=hyades_output_Convergece.txt\n")
    f.writelines("#SBATCH --ntasks="+str(n_tasks)+"\n")
    f.writelines("#SBATCH --cpus-per-task=1\n")
    f.writelines("#SBATCH --time=23:59:59\n")
    
    f2.writelines("#!/bin/bash\n")
    f2.writelines("#SBATCH --job-name=HyburnConvert\n")
    f2.writelines("#SBATCH -p scarf\n")
    f2.writelines("#SBATCH --output=convert-output.txt\n")
    f2.writelines("#SBATCH --ntasks="+str(n_tasks)+"\n")
    f2.writelines("#SBATCH --cpus-per-task=1\n")
    f2.writelines("#SBATCH --time=23:59:59\n")
#Commands for creating Hyades Batch file scripts
    for n in filenames:
        f.writelines("srun -n1 --exclusive hyades -c "+scarfPATH+n+" &\n")
        #Commands for converting to cdf file
        f2.writelines("ppf2ncdf "+scarfPATH+n[0:-3]+"ppf\n")
    f.writelines("wait")
    f2.close()
    f.close()


filePATH = "data/opacityConvergence/"
no_groupSteps = 50

filenames = get_filenames(no_groupSteps, PATH = filePATH)

init_files(filenames, original_f,PATH = filePATH)
genSweep(filenames,no_groupSteps,original_f, PATH=filePATH)

gen_scarf_batch_file(filenames)
gen_cdf_list(filenames, PATH = filePATH)
