#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 8: Lists - second test"



'''
8.5 
1) Open the file mbox-short.txt and 
2) read it line by line. 
3) When you find a line that starts with 'From ' like the following line:
        From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
4) You will parse the From line using split() and 
5) print out the second word in the line 
   (i.e. the entire address of the person who sent the message). 
6) Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
'''


print
print

count = 0

filename = raw_input('Please supply the filename: ')
fh = open(filename)

for line in fh:
    if line.startswith('From '):
        linelist = line.split()
        print linelist[1]
        count = count + 1

print 'There were',count,'lines in the file with From as the first word'


# here is another way to accomplish the same thing
# Again, Dr. Chuck's code parses every single line of the input file, and then
# performs the 'From ' check.

# The advantage is, I think, that this code's easier to maintain,
# because the if logic only does one thing, and can be changed without affecting
# the parsing/preparation of the text.

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words[0] != 'From ':continue
    print words[1]
    
# ... Oh no! this code will fail when it encounters a blank line!
# So we add a guardian pattern, a safety check - a bit like try/except but less
# full-on

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words == []: continue
    if words[0] != 'From ': continue
    print words[1]
    
# a guardian could also live above words.split() like this: 
#           if line == '': continue



print
print

print "=================================================="