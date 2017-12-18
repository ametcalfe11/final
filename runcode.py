from finalcode import*

data = open("grades.csv", 'r')
lines = data.readlines()
current_grades = []
desired_letters = []
worth_grades = []

for i in range (0,len(lines)):
	info = lines[i].rstrip().split(",") 
	current_grades.append(info[0])
	desired_letters.append(info[1])
	worth_grades.append(info[2])


print grade_needed(current_grades,desired_letters,worth_grades)