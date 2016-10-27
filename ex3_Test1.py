score_input = raw_input("Enter Score: ")

try:
	score = float(score_input)
except:
    print "Input value is not a number. Program will now exit."
    quit()

if score > 1.0: quit()
    
    
if score >= 0.9:
    print "A"
elif score >= 0.8:
    print "B"
elif score >= 0.7:
    print "C"
elif score >= 0.6:
    print "D"
else:
    print "F"