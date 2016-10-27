#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Exercise 3.3: Try and Except"

print
print

# This is an example of bad code, because part of the TRY can execute even
# though other parts will fail.

astr = 'bob'

try:
    print 'Hello'
    istr = int(astr)
    print 'There'
except:
    istr = -1
    
print 'Done',istr
    


print
print

print "=================================================="