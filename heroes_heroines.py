# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:51:38 2019

@author: vedant bonde
"""

import sys


inputfile = "corpus.txt"
names = []
file = open(inputfile, "r")
N = input()
words = []
for line in sys.stdin:
    names += [line.split()[0]]
file = open(inputfile, "r")
for line in file:
    words += line.split()
file.close()

checkinglength = 2
titleweight = 250
drweight = 200
namedict = {}

wordweights = {'Kriplani': -1, 'Sultana': -1, 'Pandit,': -1, 'Montacute,': -1, 'Reddy': -1, 'Deshmukh.': -1, 'know': -1, 'Asaf': -1, 'Amrit': -1, 'ranks': -2, 'Makhanji': -1, 'Hawken,': -1, 'Waddedar,': -1, 'away': -1, 'ruled': -1}

for name in names:
    namedict[name] = 0

checking = 0
lastword = ''
for word in words:
    if word in names:
        checking = checkinglength
        name = word
        if "Mrs" in lastword or "Miss" in lastword:
            namedict[name] -= titleweight
        elif "Mr" in lastword:
            namedict[name] += titleweight
        elif "Dr" in lastword:
            namedict[name] += drweight
    elif checking > 0 and word in wordweights:
        namedict[name] += wordweights[word]
    checking -= 1
    lastword = word
    
for name in names:
    if namedict[name] < 0:
        print ("Female")
    else:
        print ("Male")