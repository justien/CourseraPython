#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 8: Lists- Finding Averages, Splitting"

print
print

# First the old school way, the code floats through an unstructured void,
# knitting together a couple of values as it goes.  
# This version is light on memory, as it only maintains four variables each 
# time through the loop.
# total = 0
# count = 0
# while True:
#     inp = raw_input('Enter a number, or done to find average and exit: ')
#     if inp == 'done' :break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     
# average = total/count
# print 'Average of entered numbers is:', average


# Now the code uses lists, and at the end of the operation, some history of
# the voyage of the code is in existence.
# This is potentially heavy on memory, as numlist is both maintained and 
# incremented in length each time through the loop.
# numlist = list()
# while True:
#     inp = raw_input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist)/len(numlist)
# print 'Average of the number list is:',average
# print numlist

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
    print words
    print words[2]

print
print

print "=================================================="