# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:15:59 2022

@author: luisa
"""
#Homework 1
"""
Part 1:
Extract FASTA sequence of your phage genome
Find all major repeats in your phage sequence
Major repeats defined as
a. greater than 10 bp long (could be longer)
b. repeated at least three times (could be much longer)
For each major repeat, record in a Tab delimitated file:
1. The phage name
2. the repeat sequence
3. Starting base # for each occurrence
4. Closing base # for each occurrence """

import re
#Open file 
file1 = open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\Mycobacterium_phage_Airmid.fasta", "r")
fasta = file1.read()

#Get phage
pattern= re.compile(r"[a-z,M,A]{5,13}(?=\s)")
organism= pattern.findall(fasta)
phage = " ".join(organism)

#get sequence without header
def get_sequence(sequence):
    sequence_list= sequence.splitlines()
    parsed_sequence= [] 
    for line in sequence_list: 
        parsed_sequence.append(line.split())
    i=0
    seq= "" #empty string
    for line in parsed_sequence:
        if i > 0:
            seq += seq.join(line)
        i += 1
    return seq

comp_seq= get_sequence(fasta)
seq_list = [comp_seq]

#Function to get fragments of 10 aa (sliding window)
def get_window(sequence, start_index, window_size):
    i= start_index
    window= ""
    for aa in sequence:
        if len(window) < window_size:
            window += sequence[i]
            i+=1
    return window

#test = get_window(comp_seq, 0, 10)

#Function to search for specific fragment inside the complete sequence
def find_repeat(sequence, fragment):
    count = 0
    for aa in sequence:
        match = re.findall("(%s)" % fragment, aa)
        if match:
            count +=1
    return count

#test2 = find_repeat(seq_list, test)

#Function to find indexes
def find_index(sequence, fragment):
    index = 0
    for aa in sequence:
        match = re.match("(%s)" % fragment, aa)
        if match:
            index = match.span()
    return index
    
#test3 = find_index(seq_list, test)

#function to convert tuple to string
def join_tuple_string(strings_tuple):
   return ''.join(strings_tuple)


#function  to create file
def write_doc(data):
    with open("file.tsv", "a+") as f:
        f.write(data[0] + "\t" + data[1] + "\t" + data[2] + "\t" + data[3] + "\n")

#Loop to call all funtions

start= 0
size= 10
i= 0
for i in range(len(comp_seq)):
    repeat= get_window(comp_seq, start, size)
    matches= str(find_repeat(seq_list, repeat))
    indexes= find_index(seq_list, repeat)
    
    indexes_str = join_tuple_string(str(indexes))
    
    #Create list to store all variables
    output=[]
    output.append(phage)
    output.append(repeat)
    output.append(matches)
    output.append(indexes_str)
    
    doc= write_doc(output)
    
    start +=1
    i +=1
    if start == len(seq_list) - size:
        size+=1
    




















