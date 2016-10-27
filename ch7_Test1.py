#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 7: Files Assignment"

print
print

'''
7.2 
Write a program that 
1) prompts for a file name, then 
2) opens that file and reads through the file, looking for lines of the form:
   X-DSPAM-Confidence:    0.8475
3) Count these lines and 
4) extract the floating point values from each of the lines and 
5) compute the average of those values and 
6) produce an output as shown below. 


Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at 
http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name. Comment comment
'''

fname = raw_input('File for DSPAM confidence analysis: ')

try:
    fh = open(fname)
except:
    print 'File not found. Now exiting.'
    exit()

count = 0
running_total = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence'):
        cpos = line.find(':')
        score = float(line[cpos+1:])
        running_total = running_total + score
        count = count + 1

average = running_total / count
print 'Average spam confidence:',average    

print
print

print "=================================================="