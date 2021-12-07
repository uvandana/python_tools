#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:47:51 2021

@author: vandanauttamchand
"""

"""
find the common items in the list of spices and print those.

using a for loop to iterate through each item in the list
use conditional statements to compare the two and identify whether the current item is present in both.
and print list of common spices
also, find the position of "Basil" in spice_list1


"""


spice_list1 = [ 'cardamom', 'cinnamon', 'basil', 'cumin', 'pepper', 'turmeric', 'fennel', 'coriander', 'thyme', 'basil', 'mustard']
spice_list2 = ['zatar', 'paprika', 'pepper', 'basil', 'chai', 'cinnamon'  ]

common_spices = []
common_spices_dict = {}
sub_count = 0
sub_count2 = 0



for item in spice_list1 :
    if item == 'basil' :
        print('basil is at', sub_count)
    sub_count = sub_count + 1
    if item in spice_list2 :
        common_spices.append(item)
        if item in common_spices_dict :
            common_spices_dict[item] = 1 + common_spices_dict[item]
        else :
            common_spices_dict[item] = 1
        print(item, "is in both lists")
print(common_spices, common_spices_dict)

for stuff in spice_list2 :
    if stuff == 'basil' :
        print('basil is at', sub_count2)
    sub_count2 = sub_count2 + 1

        
    #else :
        #print(item, "is not present in both lists")
        
        