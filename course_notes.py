#  -*- coding: utf8 -*-
# justine lera 2016

print "=================================================="
print "Coursera Python for Everybody - Notes

print
print

Ex1
ToDo:
Tab complete doesn't work how I expect on  my Mac

loops use ITERATION VARIABLES
sequential, repeated, conditional sections of a program

----== ==---------------------------------------------------------------------
----== Chapter 2.1 Expressions ==---------------------------------------------

----> Constants
	Fixed values are called constants
	Numeric constants are numbers
	String contstants use single or double quotes 'hello' or "hello"

----> Variables
a memory location used to store a value
variable values are set with an assignment statement, such as x = "hello"
Rules:
    * start with letter or underscore
    * composed of letters, numbers and underscores
    * case sensitive
    
----> Reserved words that cannot be used as variables
	and del for is raise
	assert elif from lambda return
	global break else not try
	class except if or while
	continue exec import pass yield
	def finally in print

----> Assignment statements
	Values are assigned to variables using assignment statements

----> Numeric Expressions
	+ addition
	- subtraction
	* multiplication
	/ truncating division THIS WILL CHANGE IN PYTHON 3.0
	% remainder/modulo
	** exponentiation

----> Operator Precedence
	| Parenthesis
	| Power (exponentiation)
	| Multiplication, division, remainder
	| Addition and subtraction
	V Left to Right

----> Mixing Integer and Floating Point
	Whenever there is a floating point number in an expression, fp takes over.
	So, 99 / 100 = 100
	but 99.0 / 100 = 0.99
	
----> What does Type mean?
	Variables, literals and constants have a type.
	Python knows the difference between an integer and a string
	+ will add integers and concatenate strings
		>>> eee = "hello " + "there"
		>>> print eee
		hello there
		
	We can ask what type something is by using the function type() like this:
		>>> eee = 'hello ' + 'world'
		>>> eee = eee + 1
		Traceback ....
		>>> type(eee)
		<type 'str'>

----> Type Conversions
	Mixing an integer and float will implicitly convert a int to a float
	Also explicitly:
		>>> print float(99)/100
		0.99
		>>> i = 42
		>>> f = float(i)
		>>> print f
		42.0
		>>> print 1 + 2 * float(3)/4 -5
		-2.5
		
----> String Conversions
	str() and int()
	
----> User Input
	raw_input is a function that takes the input and converts it to a string
	name = raw_input("What is your name? ")
	print "Welcome",name
	
		inp = raw_input('Europe floor? ')
		usf = int(inp) + 1
		print 'US Floor =",usf

----> Comments in Python
	Anything after a # is ignored by Python until the next EOL
	
----> String Operations
	+ inplies concatentation
	* implies multiple concatenation
		>>> print 'Hi' * 5
		HiHiHiHiHi
		
----> Mnemonic Variable Names
	Try to use good variable names :)
	Obfuscation could be good if that's what you need!


----== ==---------------------------------------------------------------------
----== Chapter 3.1 Conditional Statements ==----------------------------------

----> Comparison Operators
    You can put if statements in two ways
        if x > 4:
            print "Hello friend"
            
        if x > 4:print "Hello friend"
        
----> Indentation
    Syntactically significant
    Maintain indentation to indicate the SCOPE of the block
    The indentation means that you don't have to end ifs/fors with an end
    Blank lines are ignored
    
----> Nested decisions
    One-way decisions
    Two-way decisions
        x = float(raw_input("Hi can I has a number plz? "))
        if x > 4.5:
            print 'You are more than four and a half'
        else:
            print 'You are not yet half-way up the stairs'
        print 'that could be all, tksom'
    Multi-way decisions
        x = float(raw_input("Hi can I has a number plz? "))
        if x < 2:
            print 'Smaller than 2'
        elif x < 10:
            print 'Equal to or larger than 2 and less than 10'
        else:
            print 'Equal to or larger than 10'
        
----> Try/Except structure
    Surround a dangerous section of code with try and except
    Put as little in the try block as possible!!!
        $ cat notry.py
        astr = 'Hello'
        try:
        	istr = int(astr)
        except:
        	istr = -1  <----- set var to a correct type but useless value
        print 'First string ",istr
        
        astr = '123'
        try:
        	istr = int(astr)
        except:
        	istr = -1
        print 'Second string ",istr
  
        
----== ==---------------------------------------------------------------------
----== Chapter 4: Functions ==------------------------------------------------
	A function is some reusable code that takes argument/s

	Say you use the builtin function called 'max()' that finds the highest 
	lexigraphic value in a string.
	It can be used in an assignment statement, like:
    	big = max('Hello world')
	    print big
	    
	When called, fns take arguments, for instance max('Hello world') has
	the argument Hello World.
	These arguments are assigned to parameters.
	A parameter is a variable used in the fn definition.
	When invoked, the parameter is given the argument value, and the fn
	can then use the value to do its work.

----> Return Values
	Stuff that the fn chucks back to the main prog.
	A fn that returns a value is called fruitful, otherwise it's called void.
		def greet(lang):
			if lang == 'es':
				return 'Hola'
			else :
				return "Hello"
			
		print greet(en), "Glenn"
		print greet(es), "Sally"
    
----> When to use functions?
	Any common chunks of code should be stuck into a library of functions.


----== ==---------------------------------------------------------------------
----== Chapter 5: Loops and Iteration ==--------------------------------------
	Repeated steps
		n = 5
		while n> 5:
			print n
			n = n -1
		print 'blastoff!'
		print n
	
----> Controlling Loop Execution
	* Using BREAK
	The break statement ends the current loop and jumps to the statement 
	immediately following. It's a test that can happen anywhere in the body
	of the loop.
		while True:
			line = raw_input('> ')
			if line == 'done':
				break
			print line
		print 'Done!'

	* Using CONTINUE
	The continue statement ends the current iteration and jumps to the top of
	the loop to start the next iteration.
	When continue's statement is True, the pointer is returned to the top of
	the containing indentation.
		while True:
			line = raw_input('> ')
			if line[0] == '#': <----checks if line's 0th element is #
				continue
			if line == 'done':
				break
			print line
		print 'Done!'
		
----> Definite Loops
	If there is a set of things through which we will check, this can be used as
	an index to control a loop, making it definite.
	Definite loops iterate through the members of an ordered set.
	They use iteration variables, which change each time by moving through the 
	members of a sequence (an orderd set).
		for i in [5,4,3,2,1]:
			print i
		print 'Blastoff!'
		
		friends = [Esmail,Remi,Deeray,Sue]
		for friend in friends:
			print 'Happy New Year ',friend
		print 'Done!'

----> Loop Idioms
	The trick is knowing something about the whole loop because you are stuck 
	writing code that only sees one entry at a time (theorem that a program
	cannot prove itself).
	
	* Counting in a loop
	To count how many times we execute a loop, we introduce a COUNTER VARIABLE
	that starts at 0, and we add 1 to it each time through the loop.
		zork = 0
		for thing in [5,3,4,5,6,8]:
			zork = zork + 1
			print zork, thing
		print 'Total count',zork
		
	* Summing in a loop
	Here, we use a sum variable, that is increased by the value of the 
	current set member with each iteration of the loop.
		zork = 0
		for thing in [5,6,4,3,8]:
			zork = work + thing
		print 'Total:',zork
		
	* Finding the Average in a loop
	An average combines the counting and sum patterns, and divides one by the
	other at the end of the loop.
		count = 0
		sum = 0
		for value in [3,5,4,2,6,7]:
			count = count + 1
			sum = sum + value
		print 'Average is:',sum/count
		
	* Filtering in a loop
	We can use an IF STATEMENT to catch or filter the values we are seeking.
		for value in [3,5,6,8,3,8]:
			if value > 7:
				print 'big number',value
		print 'Done'
		
	* Search using a Boolean variable
	Start with a variable set to False, and set it to True once value is found.
		found = False
		for value in [3,5,6,8,3,8]:
			if value ==3:
				found = True
				print '%d has been found' % value
		print 'Done'
		
	* Search using BREAK
	You can also using dump out of the loop once the term has been found.  Good
	if you only care about the first instance of a search term.
		for value in [3,5,6,8,3,8]:
    	if value == 3:
        	print '%d has been found' % value
        	break
		print 'Done'
		
	* Finding the LARGEST value
	In the largest value, setting our variable to 0 makes use of a property of
	0 relative to any set of positive numbers - that 0 will *always* be smaller.
	This guarantees that the first comparison will result in the variable
	increasing, which is what we want it to do when our comparison is True in 
	all the other cases.
	In other words, what it will do in all subsequent cases must be the same
	kind of thing that happens in the first case.
		largest = 0
		for value in [3,5,6,8,3,8]:
			if value > largest:
				largest = value
		print 'Largest:',largest
		
	* Finding the SMALLEST value
	This is trickier, and not just the opposite of the largest value approach.
	In the largest value, we leveraged the property of 0 - that it is always the
	smallest of any set of positive numbers - to guarantee that the first round
	of the loop contains a value that will make the test True.
	However, apart from infinity, there is no number that we can choose which
	will always be the largest of any set of positive numbers.  In other words,
	there is no generic value we can use to kick things off.
	Therefore we can't use a generic value (like 0).  Instead, we'll have to use
	the first member of the set to kick things off.  The only way to access this
	is to use list[0] ... /outside the loop/.  If we do it inside the loop, the 
	value will keep getting set to element[0].
		list = [3,5,6,8,3,8]
		smallest = list[0]
		for value in list:
			if value < smallest:
				smallest = value
		print 'Smallest',smallest
		
	Oh!  Python has its own way of doing this!  NONE - a new type, its own type.
		smallest = None
		for value in [3,5,6,8,3,8]:
			if smallest is None:
				smallest = value
			elif value < smallest
				smallest = value
		print 'Smallest',value
		
	But really??!?! You could do this same pattern with any value, surely ...
		smallest = 0
		for value in [3,5,6,8,3,8]:
			if smallest == 0:
				smallest = value
			elif value < smallest
				smallest = value
		print 'Smallest',value

----> A note about IS and IS NOT operators
	Python's IS can be used in logical expressions.
	It means "is the same value and type as".
	It is similar to, but stronger than '=='
	Beware of using it, as it can give you a yes when you might expect a no.
	
	
----== ==---------------------------------------------------------------------
----== Chapter 6: Strings ==--------------------------------------------------

----> Addressing positions within strings
	Get to certain places using the square bracket [0]
	Say this as fruit sub one = fruit[1]
		fruit = 'banana'
		letter = fruit [1]
		print letter 
		a
			
----> Len Function
	len(fruit) is 6
		x = len(fruit)
		print x
		6
		
----> Looping through strings
	Using a while statement and an iteration variable, and the len fn, we can 
	make a loop to look at each of the string elements individually.
		fruit = 'banana'
		index = 0
		while index < len(fruit)
			letter = fruit[index]
			print index,letter
			index = index + 1
			
	Using a FOR LOOP
	The iteration varibale is taken care of by the for loop.
		fruit = 'banana'
		for letter in fruit:
			print letter
			
----> Looping and Counting
	A simple pattern
		word = 'banana'
		count = 0
		for letter in word:
			if letter == 'a'
				count = count +1
			print count
			
----> Looking deeper into IN
	The iteration variable iterates through the sequence.
	The block of code is executed once for each value IN the SEQUENCE.
	The iteration variable moves through all the values IN the SEQUENCE.

----> SLICING through strings
	We can pul out substrings using slicing, with the colon operator.
	The slice variable is 'up to but not including'.
	If the second number is beyond the length of the string, it stops at the end
		s = 'Monty Python'
		print s[0:4]
		Mont
		print s[6:7]
		P
		print s[6:200]
		Python
		
----> String Concatenation
	Adding strings together to make a longer string
		a = 'Hallo'
		b = a + 'there'
		print b
		Hellothere
		
----> Using IN as an operator
	In can be used to check if one string is in another string.
	It is a logical operator which returns either True or False
		a = 'banana'
		if 'a' in fruit
			print 'Found it!'
			
----> String comparison
	
----> String library
	Lots of builtin stuff you can do with strings
		greet = 'Hello Bob'
		zap = greet.lower() <---- greet is not changed, btw
		print zap
		hello bob
		
	How to find all the methods in a function's library?
		stuff = 'Hello world'
		type(stuff)
		<type 'str'>
		dir (stuff)
		......  a whole bunch of string methods!
	
----> Searching a string
	We use the find function to search for a substring within a string
	.find() locates the first occurance of the substring
	not there?  returns -1
		fruit = 'banana'
		pos = fruit.find('na')
		print pos
		2
		pos = fruit.find('za')
		print pos
		-1
		
----> Search and Replace
	.replace() finds all instance of the search term and replaces it
		greet = 'Hello Bob'
		newgreet = greet.replace('Bob','Jamilla')
		print newgreet
		Hello Jamilla
		oddgreet = greet.replace('o','X')
		print odd greet
		HellX BXB

----> Stripping whitespace
	.lstring() and .rstrip() to the left and right only
	.strip() removes starting and trailing whitespace
	
----> Prefixes
	.startswith() returns True or False for the search term at the beginning of
	the string.
	

----== ==---------------------------------------------------------------------
----== Chapter 7: Files ==----------------------------------------------------

----> Using open()
	The generic form is : handle = open(filename, mode)
	Here's an example -- fhand = open('mbox.txt','r')
	Open() doesn't then pull all the data into a new memory location; instead, 
	it creates a way to step through it ...
	The thing that comes back from the open() request is the thing that 
	maintains its connection to where all the data is.  It's a pointer.
		fhand = open('mbox.txt','r')
		print fhand
		<open file 'mbox.txt' ,mode 'r' at 0x1005088b0>

	mode is optional: 'r' is to read the file, 'w' to write to the file		
	In conclusion, open() returns a handle used to manipulate the file.
	
----> The NEWLINE character
	\n is a single-character-wide symbol indicating that we go to a new line.
	When calling len(), \n counts as 1.
	
----> File Handle as a sequence
    * A file handle open for reading can be treated as a sequence of strings 
    where each line in the file is a string in the sequence.
    * We can use the FOR statement to iterate through a sequence.
    * Remember - a sequence is an ordered set.
    
    	xfile = open('mbox.txt')
    	for cheese in xfile
    		print cheese
    		
----> PATTERN - Counting Lines in a file
	* Open a file as read-only
	* use a FOR loop to read each line
	* Count the lines and output the result
	
		fhand = open('mbox.txt')
		count = 0
		for line in fhand:
			count = count + 1
		print 'Line count of %s is: ' % fhand, count

----> PATTERN - Reading the ENTIRE file
	It is possible to read a whole file, newlines and all, into a single string.
	
		fhand = open('mbox-short.txt')
		imp = fhand.read()
		print len(inp)
		print inp[:20] <-- like 'top' in bash
	
----> PATTERN - Searching through a file
	We can search through a file and print out the lines that fit a condition.
	BUT!  Each of those lines has a \n at the end.
	      And the 'print' command also includes an implicit newline ...
	      So - the following loop will insert blanks between each output line.
	      
		fhand = open ('mbox-short.txt')
		for line in fhand:
			if line.startswith('From:')
				print line
				
		... the solution? Use rstrip(), because a newline counts as whitespace.
		
		fhand = open('mbox-short.txt)
		for line in fhand:
			if line.startswith('from'):
				line = line.rstrip()
				print line
				
----> PATTERN - A Skipping Pattern
	* We can conveniently skip a line by using the CONTINUE statement
	
		fhand = open('mbox-short.txt')
		for line in fhand:
			line = line.rstrip()
			if not line.startwith('From:'): # Skip the uninteresting lines
				continue
			print line
	
	... I dunno, this seems to have a problem to me. It still needs to 
	apply rstrip (and any other computation) to each line before printing.
	... But I can imagine situations where text needs to be prepared before a
	test can be performed on it, to see if it should be fed into the result.

----> Using IN to select lines of text
    	fhand = open('mbox-short.txt')
    	for line in fhand:
    		line = line.rstrip.()
    		if not '@uct.ac.za' in line:
    			continue
    		print line  # somewhat similar to grep in bash

----> Prompt for the File Name and deal with Bad Input
	* People don't always enter good filenames, and sometimes they just want to
	get the hell out of dodge as well.  
	* Here's a pattern to deal with that.
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


----== ==---------------------------------------------------------------------
----== Chapter 8: Lists ==--------------------------------------------------

A List is a kind of collection, which allows us to put many values in a 
single 'variable'.

----> List Constants
	* Surrounded by a [ ] and elements separated by commas.
	* a list can have lists as elements, or be empty.
	* we can address any list element with the index operator 

----> Lists are Mutable
	* Unlike strings, lists are mutable.  We can assign the values of items in the
	sequence.
		lotto = [2,14,26,41,63]
		lotto[2] = 28
		print lotto
		[2,14,28,41,63]
		
----> Len() function
	* Tells us the number of elements of a set or sequence
	
----> Range() function
	* This generates a list of numbers that range from zero to one less than
	the parameter.  
		
		friends = ['shabnam','saskia','jessica','christina']
		print len(friends)
		4
		print range(len(friends))
		[0,1,2,3]
		
	* We can construct an index loop using FOR and an integer operator

		for i in range(len(friends)):
			friend = friends[i]
			print 'Happy New Year ',friend # this lets us know where we are
										   # in the list as we loop

----> Concatenate list
	Use + to cat lists together
		a = [cat,house,cheese]
		b = [dog,shed,bone]
		c = a + b
		print a
		[cat,house,cheese,dog,shed,bone]
	
----> Slice the list!
	* Just like in strings, the second number is "up to but not including"
		a = [19,34,3,17,29,11]
		print a[1:3], a[:3], a[3:], a[:]
		[34,3] [19,34,3], [17,29,11], [17,34,3,19,29,11]
		
----> How to list the methods :)
	* To list all the methods, type dir() on the list name.
		x = list()
		type(x)
		<type 'list'>
		dir(x)
		.... whole bunch of stuff!

----> Constructors
	* This is when you create an empty thing, then add stuff to it.
		stuff = list()
		
	* Now add elements to the empty thing.  It will be growing.
		stuff.append('book')
		stuff.append(99)
		
	* Appendations are added to the end of list
		print stuff
		['book',99] 
		
----> Checking list membership
	* IN and NOT IN, both of which return True or False
		99 in stuff
		True
		iPod not in some
		True
		
----> A list is an ORDERED SEQUENCE
	* And as such, the method .sort() can be applied, to change the list's order
		a.sort()
		print a
		[3,11,17,19,29,34]
	
----> Loads of useful builtin functions for lists
	* Quite a few functions will take a list as a parameter
	* So we don't have to build those basic loops anymore - \_ü_/ yay!
		nums = [3,41,12,9,74,15]
		print len(nums)
		6
		print max(nums)
		74
		print min(nums)
		3
		print sum(nums)
		154
		print sum(nums)/len(nums)
		25                         # note here we use integer division
		
----> PATTERN Averaging with a list
	* Using lists, the data is accumulated during the loop, and the computation
	happens after the loop completes.
		numlist = list()
			while True:
		    inp = raw_input('Enter a number: ')
		    if inp == 'done': break
		    value = float(inp)
		    numlist.append(value)

		average = sum(numlist)/len(numlist)
		print 'Average of the number list is:',average
		print numlist
		
----> Connecting strings and lists with split()
	* These two datatypes can be interconnected with split()
	* This is a bit like slice(), except where slice outputs a contiguous 
	subset of a list, split() creates a list, whose elements come from 
	a string.
		abc = ('with three words')
		newlist= abc.split()
		print newlist
		['with','three','words]
		for w in newlist:
			print w
		with
		three
		words
		
----> Features of split()
	* will ignore a lot of repeated spaces
	* can specify delimiter - split(';')

----> PATTERN The Double Split 
	* Sometimes we split a line, take one element, and then split that element.
	* For instance, find an email address, then break the address up into parts.
		words = line.split()
		email = words[1]
		pieces = email.split('@')
		domain = pieces[1]
		

----== ==---------------------------------------------------------------------
----== Chapter 9: Dictionaries ==---------------------------------------------

----> What is a Collection?
	* A List is a linear collection indexed by integers
	* A Dictionary is unsorted bag of values, each with it's own label
	* There are no ordinal values, only cardinals
	* It is a Key/Value store (wikipedia.org/wiki/associative_array)
	* It allows for fast database-like operations in Python
	    - Perl/PHP - associative array
	    - Java - Properties/Map/HashMap
	    - C#/.Net - property bag or attribute bag
	    
----> Properties of Dictionaries
	* Dictionary items are indexed by their lookup tag
	* We assign values using a LOOKUP EXPRESSION
		purse = dict()
		purse['money'] = 12
		purse['candy'] = 3
		purse['tissues'] = 75
		print purse
		{'money':12,'tissues':75,'candy':3}
		print purse['candy']
		3
		print purse['candy'] = purse['candy'] + 2
		print purse['candy']
		5
		
	* ... but note!  This is not the same as a 2d array

----> Order in a Dictionary
	* Looking up uses HASHING instead of an order
	   --> this makes DICTIONARIES FAST!!
	* When printing dictionaries, input order doesn't determine the output order.

----> Dictionary Literals (Constants)
    * Dictionary literals use curly braces and have a list of key:value pairs
    * You can make an EMPTY DICTIONARY using empty curly braces
        jjj = { }
        print jjj
        {}
    * dict() is a function, too, because you can create a dict this way:
        jjj = dict()

----> PATTERN Finding the most common name
    * z.B. Dictionaries let us keep track of a large number of counters
        ccc = dict()
        ccc['cwen'] = 1
        ccc['cwen'] = ccc['cwen'] + 1
		print ccc
		{'cwen':2}
		
----> Dictionary Tracebacks
	* Don't reference a key before it exists :D
	* We can use the IN OPERATOR to test if a key exists
		ddd = dict()
		print ccc['csev']
		 Traceback ... KeyError:'csev'
		 print 'csev' in ccc
		 False

----> PATTERN Creating entries on the fly
	* It's not possible to operate on KV pair w/o creating it first.
	* Which is a bit clunky ... ?
		counts = dict()
		names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
		for name in names:
			if name not in names:
				counts[name] = 1
			else:
				counts[name] = counts[name] + 1
		print counts

----> The GET() METHOD for Dictionary functions
	* Takes two parametes: a KEY name, and a value to give back if KEY is False
	* You glue it on to the end of any dict call:
		print count.get(name,0)		# equiv to the IF statement
									# if name in counts:
									#	print counts[name]
									# else:
									#	print 0

----> PATTERN Counting with GET()
	* We can use get() to provide a default value of 0 when the key
	doesn't yet exist in the dictionary
		counts = dict()
		names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
		for name in names:
			counts[name] = counts.get(name,0) + 1
		print counts
					... get the value at counts[name] and 
					if you don't find it, then
					create it, and 
					give it the value of 0
					... it brings the get() helper, like an assistant who
					always knows what to do in specific circumstances.
					
----> PATTERN Finding the most common element
	* SPLIT the line into words, then loop through this list using a dictionary
	to track the count of each word.
		counts = dict()
		print 'Enter a line of text:'
		line = raw_input('')
		
		words = line.split()
		print 'words:',words
		
		print 'Counting ...'
		for word in words:
			counts[] = counts.get(word,0) + 1
			
		print 'Counts',counts
		
----> Definite Loops and Dictionaries
	* Even though dictionaries are not stored in order, a FOR LOOP can iterate
	through a dictionary. It goes through the KEYS and looks up their values.
		counts = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
		for key in counts:
			print key, counts[key]	# key is not a reserved word
			
----> Retrieving lists of Keys and Values
	* It's possible to get a list of keys, values, or items from a dictionary.
		jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
		print list(jjj)
		print jjj.keys()
		print jjj.values()
		print jjj.items()
						... by the way, until an alteration changes the hash of
						the dict, .keys() and .values() will output in the
						same order.
						... so watch out for subtle bugs based on this!
						
----> Bonus!  Two Iteration Variables!
	* You can loop though the KV pairs in a dict using *2* iter vars.
	* Each iteration, var1 is the KEY and var2 the the corresponding VALUE
		jjj = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }
		for aaa,bbb in jjj.items():
			print aaa,bbb
			
----> PATTERN Identifying the most frequently occuring item in a list
	* and here we return to the code fragment from the start of the course! :D
		name = raw_input'Enter file: '
		handle = open(name)
		text = handle.read()
		words = text.split()
		
		counts = dict()
		for word in words:
			counts[word] = counts.get(word,0) + 1
			
		bigcount = None
		bigcount = None
		for word,count in counts.items():
			if bigcount = None or count > bigcount:
				bigword = word
				bigcount = count
		

	  















































----> 
----== ==---------------------------------------------------------------------
----== Chapter n: Subject ==--------------------------------------------------
print
print

print "=================================================="