import math

print "Welcome to my super duper area calulator :)"
print "n\ Please tell me what shape you would like me to calculate the area of?"
print "1. Square or Rectangle"
print "2. Circle"
print "3. Triangle"

user_shape = input("Please enter the number: ")

def action(shape):
    if shape == 1:
        print "You have chosen Square/Rectangle"
        print "I will now ask for some dimensions and units of measure"
        units = raw_input("What is the unit of measure? e.g. cm, m, inches etc... >> ")
        width = input("What is the width of this shape? >> ")
        length = input("What is the length of this shape? >> ")
        area = width * length
        print "The area of this shape is %i%s squared" % (area, units)
    elif shape == 2:
        print "You have chosen a circle"
        print "I will now ask for some dimensions and units of measure"
        units = raw_input("What is the unit of measure? e.g. cm, m, inches etc... >> ")
        radius = input("What is the radius of the circle? >> ")
        area = math.pi * (radius*radius)
        print "The area of this circle is %i%s squared" % (area, units)
    elif shape == 3:
        print "coming soon" 

action(user_shape)
