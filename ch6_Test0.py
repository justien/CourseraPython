#  -*- coding: utf8 -*-
# justine lera 2016
# Python Specialisation - Coursera

# 234567890123456789012345678901234567890123456789012345678901234567890123456789
print "=================================================="
print "Chapter 6: Strings Assignment"

print
print

# Comment comment

print """
6.5 Write code using find() and string slicing (see section 6.10) to extract 
the number at the end of the line below. 
Convert the extracted value to a floating point number.
Print it out.
"""

text = "X-DSPAM-spamidence:    0.8475";

dppos = text.find('.')
spamscore = text[dppos-1:] # assumes scores are between 1.0 and 0.0
spamscore = float(spamscore)
print spamscore

# assumes score can be any float >= 0
prefixend = text.find(':')
spamscore = text[prefixend+1:]
spamscore = spamscore.strip()
spamscore = float(spamscore)
print spamscore

# short way of doing above
spamscore = float(text[prefixend+1:].strip())
print spamscore

# float does a .strip() before type conversion
pos = text.find(':')
num = float(text[pos+1:])
print num

print
print

print "=================================================="