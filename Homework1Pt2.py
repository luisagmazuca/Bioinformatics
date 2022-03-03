# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:44:39 2022

@author: luisa
"""
"""Part 2:
Extract CDS (coding sequence) information from GenBank file, place into tab delimitated file
1. The phage name
2. the full aa sequence of the protein
3. the starting base # for the first codon
4. the closing base # for the third nt of the last codon
5. The orientation of the gene (positive or negative strand).
6. the gene name
7. the gene description (“product”)"""

import re
#Open file 
file1 = open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\Mycobacterium_phage_Airmid.gb", "r")
gbfile = file1.read()

#
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

gb_string= gbfile.splitlines() #convert to a list of strings

gb_list= [] #create 2D list
for line in gb_string: 
    gb_list.append(line.split())

#1. Get phage
phage= get_all_matched(r"(?<=DEFINITION)", gb_list, 1)

#2. Get aa sequence
translation= get_all_matched(r"[A-Z]{20,}", gb_list, 0)

trans_no_sp_chars1= translation.replace("/", "")
trans_no_sp_chars= trans_no_sp_chars1.replace("=", " ")

translation_string = trans_no_sp_chars.splitlines()

translation_full= []
merge = ""
i=0
for line in translation_string:
    if i > len(translation_string):
        break
    if line.startswith("translation"):
        merge = line
        i+=1
    if not line.startswith("translation"):
        merge += line
        i+=1
    if i>= len(translation_string):
        i-=2
    if translation_string[i].startswith("translation"):
        translation_full.append(merge)

#3 & 4 star and end
start_end = get_all_matched(r"(CDS)", gb_list, 0)
st_end_list= start_end.splitlines()

stend= ""
startend= []
for line in st_end_list:
    if line.startswith("CDS"):
        stend= line.replace("CDS", "")
        startend.append(stend)
        
#6 gene name
gene= get_all_matched(r"(/gene)", gb_list, 0)
gene_list= gene.splitlines()

#7 description -> product
prod= get_all_matched(r"(/product)", gb_list, 0)
product= prod.splitlines()
