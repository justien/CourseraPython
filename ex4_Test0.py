#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 4: Functions"

print
print

'''
4.6 Write a program to prompt the user for hours and rate per hour using 
raw_input to compute gross pay. Award time-and-a-half for the hourly rate 
for all hours worked above 40 hours. 

Put the logic to do the computation of 
time-and-a-half in a function called computepay() and use the function to do 
the computation. 

The function should return a value. 

Use 45 hours and a rate 
of 10.50 per hour to test the program (the pay should be 498.75). 

You should 
use raw_input to read a string and float() to convert the string to a number.
 
Do not worry about error checking the user input unless you want to - you can 
assume the user types numbers properly. 

Do not name your variable sum or use 
the sum() function. 
'''

def compute_pay(hours, rate):
    if hours <= 40.0:
        pay = hours * rate
    else:
        overtime_hours = hours - 40
        pay = (40 * rate) + (overtime_hours * (rate * 1.5))
    return pay
    
hours_input = raw_input("How many hours were worked this week? ")
hours = float(hours_input)

rate_input = raw_input("What is the base hourly rate? ")
rate = float(rate_input)

print "The pay due is: ",compute_pay(hours, rate)



print
print

print "=================================================="