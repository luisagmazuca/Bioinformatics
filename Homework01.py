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

#Open file 
file1 = open("C:\\Users\\luisa\\Documents\\Spring 2022\\BINF II\\Lab\\Mycobacterium_phage_Airmid.fasta", "r")
fasta = file1.read()

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

#Function to get fragments of 10 aa (sliding window)
def get_window(sequence, start_index, window_size):
    i= start_index
    window= ""
    for aa in sequence:
        if len(window) < window_size:
            window += sequence[i]
            i+=1
    return window

test = get_window(comp_seq, 0, 10)

#Function to search for specific fragment inside the complete sequence

#functio  to create file

#Loop to call all funtions





















