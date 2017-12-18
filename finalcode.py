import sys

def grade_needed(current, desired, worth):
	for i in range (0,len(current)):
		print "If your current grade is " + str(current[i])+ "%, your final is worth "+ str(worth[i]) + "%, and you want a/an " + str(desired[i])+ "."
		currentweight= (100- float(worth[i]))/float(100)
		step1= float(current[i])*currentweight

		if desired[i]=="A":
			step2= 90-float(step1)
		if desired[i]=="B":
		 	step2= 80-float(step1)
		if desired[i]=="C":
		 	step2= 70-float(step1)
		if desired[i]=="D":
		 	step2= 60-float(step1)
		if desired[i]=="F":
		 	step2= 50-float(step1)
		
		divideby= float(worth[i])/float(100)
		step3=float(step2)/divideby
		print "You will need a " +str(step3) +"% on the final."
		
			

