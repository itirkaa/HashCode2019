# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:36:42 2019

@author: Arijit Aakriti
"""
with open('e_shiny_selfies.txt', 'r') as f:
    content = f.readlines()

content = [x.strip() for x in content]
content.pop(0)
slide_h = []
slide_v = []
h_count, v_count = 0, 0
for index in range(len(content)):
    if content[index][0] == 'H':
        h_count += 1
        slide_h.append(index)
    elif content[index][0] == 'V':
        v_count += 1
        slide_v.append(index)

sum = int(h_count + v_count/2)

file = open("outpute.txt","w")
file.write(str(sum))
for index in range(len(slide_h)):
    file.write("\n".join(str(slide_h[index])))
for index in range(0,len(slide_v)-1,2):
    file.write("\n".join(str(slide_v[index])+" "+  str(slide_v[index+1])))
file.close()