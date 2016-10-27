#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 9: Assignment - Dictionaries"

print
print

'''
9.4 Write a program to :
1) read through the mbox-short.txt and 
2) figure out who has the sent the greatest number of mail messages. 

The program looks for 'From ' lines and 
takes the second word of those lines as the person who sent the mail. 

The program 
1) creates a Python dictionary that 
2) maps the sender's mail address to a 
3) count of the number of times they appear in the file. 

After the dictionary is produced, the program reads through the dictionary using
a maximum loop to find the most prolific committer.
'''

emailhist = {}

# open the file
name = raw_input('Enter the name of the file:')
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)


# find From email addresses, and populate a dict with their freq histogram
for line in fhand:
    if not line.startswith('From '):continue
    words = line.split()
    email = words[1]
    emailhist[email] = emailhist.get(email,0) +1

# find the highest frequency email and display results as 
# '<email address> <frequency>'

highcount = None
highaddress = None
for address,count in emailhist.items():
    if highcount == None or highcount < count:
        highcount = count
        highaddress = address
        
print highaddress,highcount





    





# loop to 



# loop to count up the frequency of each email address


# loop to identify the email address with the highest frequency


print
print

print "=================================================="