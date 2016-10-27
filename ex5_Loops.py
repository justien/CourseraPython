#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Lecture 5: Loops and Iteration"

print
print

# This is to test the exact shape of CONTINUE within various loops.

# sytax error - BREAK is outside loop

# user_input = raw_input('Enter a word. \'Q\' will quit, \'#\' will ignore: ')
# if user_input[0] == 'Q':
#     break
# if user_input[0] == '#':
#     continue
# print user_input

# just a loop
while True:
    user_input = raw_input('Enter a word. \'Q\' will quit, \'#\' will ignore: ')
    if user_input[0] == 'Q':
        break
    if user_input[0] == '#':
        continue
print user_input
print 'The loop has been exited. Welcome to the outside.'

print
print "Finding the average"
count = 0
sum = 0
for thing in [3,5,4,2,6,7]:
	count = count + 1
	sum = sum + thing
print 'Average is:',sum/count

print
print "looking for a value"
found = False
for value in [3,5,6,8,3,8]:
	if value == 3:
		found = True
		print '%d has been found' % value
print 'Done'

print
print "Looking for a value using BREAK"
found = False
for value in [3,5,6,8,3,8]:
    if value == 3:
        print '%d has been found' % value
        break
print 'Done'

print

print "Looking for the smallest, use arbitrary initial value"

smallest = 0
for value in [-11,-119, 5,6,8,2,8]:
    print 'The For Loop: Value, smallest',value, smallest
    if smallest == 0:
        smallest = value
        print "Smallest after first comparison",smallest
    elif value < smallest:
        smallest = value
        print "Smallest, value",smallest, value
print 'Smallest',smallest

print
print

print "=================================================="