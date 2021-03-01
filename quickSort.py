# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:41:14 2019

@author: harshvardhan
"""

def Partition(array,start,end):
    pivot = array[start]
    left = start
    right = end
    while(left<=right):
        while(array[left]<=pivot):
            left+=1
        while(array[right]>pivot):
            right-=1
        if left<right:
            temp = array[left]
            array[left] = array[right]
            array[right]=temp
     
    temp2 = array[start]
    array[start]=array[right]
    array[right]=temp2
    
    return right

def QuickSort(array,start,end):
    if(start<end):
        j=Partition(array,start,end)
        QuickSort(array,start,j)
        QuickSort(array,j+1,end)
        
        

ls = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950]

ans = QuickSort(ls,0,len(ls)-1)