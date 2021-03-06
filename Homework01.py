# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:15:59 2022

@author: luisa
"""
#Homework 1
#Part1
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
    seq= ""
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
        #if start_index> len(sequence)-window_size:
            #break
        if len(window) < window_size:
            window += sequence[i]
            i+=1
    return window

#Function to search for specific fragment inside the complete sequence
def get_repeat(sequence, fragment):
    count = 0
    for match in re.finditer("(%s)" % fragment, sequence):
        count += 1
    return count

#Function to find indexes
def get_index(sequence, fragment):
    index = ();
    for match in re.finditer("(%s)" % fragment, sequence):
        index += match.span()
    return index

#function to convert tuple to string
def join_tuple_string(strings_tuple):
   return ''.join(strings_tuple)

#function  to create file
def write_doc(data):
    with open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\file.tsv", "a+") as f:
        f.write(data[0] + "\t" + data[1] + "\t" + data[2] + "\t" + data[3] + "\n")

#Loop to call all funtions
start= 0 #start index in the string
size= 10 #size of the sliding window, will be input for function get_window
check_repeats= [] #empty list to store repeats to make sure they are not repeated
i=0
while i < len(comp_seq):
    
    if size > (len(comp_seq)/3):
        break
    if start > ((len(comp_seq))-size): #meaning that there is no more space for another repeat towards the end of the string
        size +=1 
        start = 0
        i=0
    
    repeat= get_window(comp_seq, start, size) #selects a window
    matches= get_repeat(comp_seq, repeat) #counts how many times
    indexes= get_index(comp_seq, repeat) #at which index it's found
    indexes_str = join_tuple_string(str(indexes)) #converts touple indexes to string
    
    #Create list to store all variables
    if matches >= 3 and repeat not in check_repeats:
        output=[]
        output.append(phage)
        output.append(repeat)
        output.append(str(matches))
        output.append(indexes_str)
        
        write_doc(output)
        if repeat not in check_repeats:
            check_repeats.append(repeat)
            
    start +=1
    i+=1