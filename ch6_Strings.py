#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 6: Strings - Parsing Text"

print
print

# Comment comment

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

atpos = data.find('@') # tell us where the @ is
print atpos

sppos = data.find(' ',atpos) # start at position 21 and look for next space 
print sppos

host = data[atpos+1 :sppos] # give me from just after the @ to the next space
print host                  # we're SLICING a bit out of the string!!

x = 'From marquard@uct.ac.zy'
print x[8]
print x[14:17]

greet = 'Hello Bob'
print greet.upper()

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print data[pos:pos+3]


print
print

print "=================================================="