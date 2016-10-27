#  -*- coding: utf8 -*-
# justine lera 2016

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Exercise 3: Test"

print
print

hours_input = raw_input("Enter Hours: ")
hours = float(hours_input)
overtime_hours = hours - 40
print "Hours worked:",hours
print "Overtime hours: ",overtime_hours

print

rate_input = raw_input("Please enter the regular hourly rate: ")
rate = float(rate_input)
overtime_rate = rate * 1.5
print "Base Rate:",rate
print "Overtime Rate:",overtime_rate

pay = 0.0
print "Current Pay:",pay

print

if hours <= 40.0:
    pay = hours * rate
else:
    overtime_hours = hours - 40
    print overtime_hours
    pay = (40 * rate) + (overtime_hours * overtime_rate)

print pay


print
print

print "=================================================="