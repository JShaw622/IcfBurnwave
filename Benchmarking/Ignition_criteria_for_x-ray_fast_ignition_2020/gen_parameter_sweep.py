# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:04:55 2023

@author: Jack Shaw
"""

original_f = "test.inf"
#print(original_f.read())


def get_filenames(n=10):
    f = []
    filenames =[]
    #this will create the files if needed
    for i in range(10): 
        filename = "test_" + str(i)+".inf"
        filenames.append(filename)
        
        print("Making file: " + filename)
        f.append(open(filename,"w"))
    return filenames

#opens the files and copies orignal file contents to them but changes the first line to the name of the file
def init_files(names, original_filename):
    o_f = open(original_filename, "r").readlines()
    for n in names:
        print("Initialising file: " + n)
        f = open(n, "w")
        o_f[0] = n[0:-4]+"\n"
        f.writelines(o_f)
        f.close()
    
#loops through files and changes the temperature of the hotspot between init_T and final_T
def T_sweep(names, original_filename, init_T = 1, final_T = 1):
    steps = len(names)-1
    T = init_T
    T_increment =(final_T-init_T)/steps
    print(T_increment)
    
    o_f = open(original_filename, "r").readlines()
    for n in names:
        print("Temp sweep file: " + n)
        f = open(n, "w")
        o_f[11] = "DEFINE HsTemp "+str(round(T,2))+"\n"
        T+=T_increment()
        
        f.writelines(o_f)
        f.close()
        
#sweeps through radius between init_r and final_r
def r_sweep_radius(names, original_filename, init_r = 0.001, final_r=0.01):
    steps = len(names)-1
    r = init_r
    r_increment =(final_r-init_r)/steps
    print(r_increment)
    
    o_f = open(original_filename, "r").readlines()
    for n in names:
        print("Radius sweep file: " + n)
        f = open(n, "w")
        o_f[6] = "DEFINE HsRad "+str(round(r,2))+"\n"
        r+=r_increment()
        
        f.writelines(o_f)
        f.close()
        
        
filenames = get_filenames()

init_files(filenames,original_f)

T_sweep(filenames, original_f, 1, 20)



##########
Need to find a way of sweeping through radius for each temperature inciement

