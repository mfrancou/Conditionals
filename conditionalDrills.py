'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
grade=64
if(grade>65):
    print("student is passing")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
if(grade==65):
    print("student is failing")
elif(grade<65):
    print("student is failing")
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
age=17
if(age>=18):
    print("You are old enough to vote.")
elif(age<=18):
    print("You are not old enough to vote.")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
weight=1
if(weight>=1):
    print(weight*2.20462)
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
if(weight>=1):
    print(weight*0.453592)