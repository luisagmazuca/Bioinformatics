# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:48:03 2022

@author: luisa
"""

#Lab 7

import re
file= open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\lab07\\prot1.txt", "r")
prot1 = file.read()

prot1_string= prot1.splitlines()

prot1_list= []
for line in prot1_string: 
    prot1_list.append(line.split())

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

hits = get_all_matched(r"(sp)", prot1_list, 0)

hits_lines= hits.splitlines()

sig_hits = []
for line in hits_lines:
    if not line.startswith(">"):
        rep= line.replace("|", " ")
        sig_hits.append(rep)

hits_list= []
for line in sig_hits: 
    hits_list.append(line.split())

i = 0   
for line in sig_hits:
    globals()["hits_list" + str(i)] = []
    #if not line.startswith("sp"):
        #i +=1
        #continue
    if line.startswith("sp"):
        globals()["hits_list" + str(i)].append(line)
    
        

    


    
    
    
    
    
    l
