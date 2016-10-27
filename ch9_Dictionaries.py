#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 9: Dictionaries"

print
print

# Comment comment
purse = dict()
purse['money'] = 12 # purse-sub-money or purse of money
purse['candy'] = 3
purse['tissues'] = 75
print purse
{'money':12,'tissues':75,'candy':3}
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse['candy']

print 'Creating a dictionary using a dictionary literal'
print 'jjj = { }'
jjj = { }
print jjj

print

ccc = {}
ccc['ccc.cwen'] = 1
ccc['ccc.cwen'] = ccc['ccc.cwen'] + 1
print ccc

print
print 'catting strings in dicts'
ddd = {}
ddd['ddd.cwen'] = ''
ddd['ddd.cwen'] = ddd['ddd.cwen'] + 'hope'
print ddd

print
print 'Using get() to shorten FOR loops when initialising a dict'
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts

print
print 'Finding the most common element from an input'
counts = dict()
print 'Enter a line of text:'
line = raw_input('')

words = line.split()
print 'words:',words

print 'Counting ...'
for word in words:
    counts[word] = counts.get(word,0) + 1
    
print 'Counts',counts

print
print 'Definite Loops'
counts = { 'chuck' : 1 , 'shabnam' : 3 , 'saskia' : 42 }
for key in counts:
    print key, counts[key]

print
print'Dictionaries --> Lists'
jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
print 'The list',list(jjj)
print 'The keys',jjj.keys()
print 'The values',jjj.values()
print 'The items',jjj.items()
		
print
print 'Two iteration variables when using .LIST()'
jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
for aaa,bbb in jjj.items():
    print aaa,bbb
    
print
print 'Finding the most frequently occuring words in a list'
name = raw_input('Enter file: ')
handle = open(name)
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
    
bigcount = None
bigcount = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count

print bigword,bigcount


print
print

print "=================================================="