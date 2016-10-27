#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Exercise 3.3.1: Try and Except"

print
print

# on the TRY line, python will attempt the instruction.
# If it throws an error, python will discard the result of the operation, 
# and move on to the except(ion) instruction.

# In this example, the variable user_input is converted to an INT, then passed
# to the variable ival.
# However, the type conversion can result in a ValueError.
# If it does, Python will back out of the conversion, instead performing the 
# exception instruction, setting ival to -1.

user_input = raw_input('Enter a number: ')

try :
    ival = int(user_input)
except :
    ival = -1
    
if ival > 0 :
    print 'Nicework!'
else :
    print 'The input was not a number'
    

print
print

print "=================================================="