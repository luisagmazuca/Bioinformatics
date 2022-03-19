# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:25:09 2022

@author: luisa
"""
#Rebeuca

import re
file= open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\lab04\\rebeuca.predict", "r")
rebeuca = file.read()

rebeuca1= rebeuca.splitlines()

rebeuca_list= [] #create 2D list
for line in rebeuca1: 
    rebeuca_list.append(line.split())

#Extract information from predict file from GLimmer (orf, start, and stop)
orfs= []
for i in range(len(rebeuca_list)):
    orfs.append(rebeuca_list[i][0])

start = []
for i in range(len(rebeuca_list)):
    start.append(rebeuca_list[i][1])
    
stop = []
for i in range(len(rebeuca_list)):
    stop.append(rebeuca_list[i][2])

file2= open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\lab04\\rebeuca.gb", "r")
rebeuca2 = file2.read()

rebeuca_2 = rebeuca2.splitlines()

rebeuca2_list= [] #create 2D list
for line in rebeuca_2: 
    rebeuca2_list.append(line.split())

def get_all_matched(pattern, sequence, start_index):
    store = ""
    s= " "
    for arr in sequence:
        for word in arr:
            if re.search(pattern, word):
                string= ""
                string= s.join(arr[start_index:]) 
                store += string + "\n"
    return store

cds = get_all_matched(r"(CDS)", rebeuca2_list, 1)
cds1 = cds.splitlines()

start_end= []
for line in cds1:
    nodot= line.replace(".", " ")
    start_end.append(nodot)

nums= []
for line in start_end:
    if line.startswith("complement"):
        rep= line.replace("complement", "")
        nums.append(rep)
    else:
        nums.append(line)

nums1= []
for line in nums:
    if line.startswith("("):
        rep1= line.replace("(", "")
        nums1.append(rep1)
    else:
        nums1.append(line)

nums2= []
for line in nums1:
    if line.endswith(")"):
        rep2= line.replace(")", "")
        nums2.append(rep2)
    else:
        nums2.append(line)

cds_list= [] #create 2D list
for line in nums2: 
    cds_list.append(line.split())

start_gb= []
for i in range(len(cds_list)):
    if len(cds_list[i]) > 0:
        start_gb.append(cds_list[i][0])

stop_gb= []
for i in range(len(cds_list)):
    if len(cds_list[i]) > 0:
        stop_gb.append(cds_list[i][1])

#Extract information from GenBank file    
import csv

with open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\lab04\\Comparisions_Rebeuca.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

#Generates comments from a CSV file
comments= []
comment= ""
for i in range(len(data)):
    if data[i][1] == data[i][4] and data[i][2] == data[i][3]:
        comment = "complement"
        comments.append(comment)
    elif data[i][1] == data[i][2] and data[i][3] == data [i][4]:
        comment = "same gene"
        comments.append(comment)
    elif data[i][1] != data[i][2] and data[i][3] == data [i][4]:
        comment = "different start"
        comments.append(comment)
    elif data[i][1] == data[i][2] and data[i][3] != data [i][4]:
        comment = "different end"
        comments.append(comment)
    elif data[i][1] == data[i][4] and data[i][2] != data[i][3]:
        comment = "complement with different end"
        comments.append(comment)
    elif data[i][1] != data[i][4] and data[i][2] == data[i][3]:
        comment = "complement with different start"
        comments.append(comment)
    elif data[i][1] == "":
        comment = "does not exist in GenBank"
        comments.append(comment)
    elif data[i][2] == "":
        comment = "does not exist in Glimmer"
        comments.append(comment)
    else:
        comment = "different gene"
        comments.append(comment) 