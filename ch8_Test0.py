#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter nn: Asking Questions"

print
print

'''
8.4 
1) Open the file romeo.txt and 
2) read it line by line. 
3) For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
4) For each word on each line:
    a) check to see if the word is already in the list and 
    b) if not append it to the list. 
5) When the program completes: 
    a) sort and 
    b) print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

megalist =[]
fhand = open('romeo.txt')

for line in fhand:
    linelist = line.split()
    
    for word in linelist:
        if not word in megalist:  
            megalist.append(word)

megalist.sort()
print megalist

print
print

print "=================================================="