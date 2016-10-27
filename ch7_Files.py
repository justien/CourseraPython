#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 7: Files"

print
print

print
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print 'Line count of \n %s \n is: \t' % fhand, count

print
fhand = open('mbox0.txt') # the file must opened again after the above work
for line in fhand:
    print line

print
fhand = open ('mbox-short.txt')
for line in fhand:
	if line.startswith('From:'):
	    print line

print
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip() # I applied rstrip to the results to reduce the
        print line           # time taken to run the script

print   
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print line

print
while True:
    fname = raw_input('Enter the file name, or Done to exit: ')

    if not fname.lower() == 'done':    
        try:
            fhand = open(fname)
            break
        except:
            print fname,'could not be found.'
            continue
    else:
        exit()
        
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
if count == 1:
    print 'There is 1 subject line in',fname
else:
    print 'There were ',count,'subject lines in',fname

print
print

print "=================================================="