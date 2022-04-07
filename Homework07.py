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

#create a list for each query
j = 0   
for i in range(len(sig_hits)):
    if i == len(sig_hits)-1:
        break
    if not sig_hits[i].startswith("sp") and sig_hits[i+1].startswith("sp"):
        j +=1
        globals()["hits_list" + str(j)] = []
    if sig_hits[i].startswith("sp"):
        globals()["hits_list" + str(j)].append(sig_hits[i])
        
#make hits_lists splitliness
def create_query (query_number):    
    globals()["query" + str(query_number)] = []
    for line in globals()["hits_list" + str(query_number)]: 
        globals()["query" + str(query_number)].append(line.split())
    return globals()["query" + str(query_number)]

#call function
query1 = create_query(1)
query2 = create_query(2)
query3 = create_query(3)
query4 = create_query(4)

#function to check for significant e-score value
def check_score(query):
    sig_hits_query = []
    for i in range(len(query)):
        if float(query[i][len(query[i])-1]) <= 10e-6:
            sig_hits_query.append(query[i][1])
            if i == 9:
                break
        else:
            sig_hits_query.append(query[0][1])
            break
    return sig_hits_query

sig_hits_query1 = check_score(query1)
sig_hits_query2 = check_score(query2)
sig_hits_query3 = check_score(query3)
sig_hits_query4 = check_score(query4)
                

    
        

    


    
    
    
    
    
