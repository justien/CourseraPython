#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 5: Loops and Iterations, Test"

print
print

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the
# user enters 'done'. 
# 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# 
# If the user enters anything other than a valid number catch it with a try/except
#  and put out an appropriate message and ignore the number. 
#  
# Enter the numbers from the book for problem 5.1 and Match the desired output as
# shown.
#   
# Input = 4, 5, bad data, 7
# 
# Desired output:
# 
# Invalid input
# Maximum is 7
# Minimum is 4

largest = None
minimum = None

while True:
    num = raw_input("Enter a number: ")
    
    if num == "done":
        break
    
    try :
        num = int(num)
    except :
        print "Invalid input"
        continue
    
    if largest is None:
        largest = num
#        print "Largest starts at: ", largest
        minimum = num
#        print "Minimum starts at: ", smallest
    elif num > largest:
        largest = num
#        print "Largest has been increased to: ", largest
    elif num < minimum:
        minimum = num
#        print "Minimum has been decreased to: ", smallest

print "Maximum is", largest
print "Minimum is", minimum


print
print

print "=================================================="