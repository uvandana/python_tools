#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:17:46 2021

@author: vandanauttamchand
"""
"""

find duplicates from a list.
Using for loop iterate through the list of numbers and use conditional statements.
Compare list with iterated so far each time to determine if it's a duplicate.
Print the list of duplicates 

"""

word_list = [ 'ready', 'to', 'get', 'the', 'dress', 'ready', 'for', 'the', 'prom', 'the' ]
length = len(word_list)
sub = 0
occurred_dict = {}
duplicate_dict = {}


for word in word_list :
    #print(sub, word)
    sub = sub + 1
    if word not in occurred_dict :
        occurred_dict[word] = 1
    else :
        if word in duplicate_dict :
            duplicate_dict[word] = duplicate_dict[word] + 1
        else :
            duplicate_dict[word] = 1
        
        
for duplicates in duplicate_dict :
    print(duplicates, duplicate_dict[duplicates])
    
