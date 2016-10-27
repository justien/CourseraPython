#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 7: Files Assignment"

print
print

'''
7.1 
Write a program that:
1) prompts for a file name, then
2) opens that file and reads through the file, and then
3) prints the contents of the file in upper case.

 Use the file words.txt to produce the output below.
You can download the sample data at http://www.pythonlearn.com/code/words.txt
'''

# Use words.txt as the file name


fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    exit()
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print line    

print
print

print "=================================================="