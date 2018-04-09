"""
Created on Sun Mar 25 19:05:03 2018

@author: patricio
"""
import time

letter_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
           'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
           'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def compute_nm_score(name_str):
    score = 0
    for letter in name_str:
        score += letter_dict[letter]
    return score

import urllib.request as url
info = url.urlopen('https://projecteuler.net/project/resources/p022_names.txt')
nm_list = str(info.read()).replace('"','').replace("'",'').replace('b','')
nm_list = nm_list.split(',')
nm_list.sort()

start = time.time()

sum_scores = 0
for name in nm_list:
    score = compute_nm_score(name)*(nm_list.index(name)+1)
    sum_scores += score
    
print(sum_scores)

print(time.time() - start)
