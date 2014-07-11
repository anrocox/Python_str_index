#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

How to get the index of a substring contained in a str python?

¿Como obtener el indice de un substring contenido en un str python?
'''

#create a str
s = 'I wish to wish the wish'
print(s)

#the find() method return the index of the string where the
#first substring is found, return -1 if substring is not found.
index = s.find('wish')
print(index)

#define the segment of the string to perform the search
index = s.find('wish', 7, -5)
print(index)

#the index(value) method works like find() method, but raise ValueError
#when the substring is not found.
index = s.index('to')
print(index)

#difference between the two methods
print(s.find('not found'))
print(s.index('not found'))
