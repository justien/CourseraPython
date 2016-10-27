#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Exercise 3.3.1: Try and Except"

print
print

# Comment comment

rawstrng = raw_input('Enter a number: ')

try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0:
    print 'Nicework!'
else:
    print 'The input was not a number'
    

print
print

print "=================================================="