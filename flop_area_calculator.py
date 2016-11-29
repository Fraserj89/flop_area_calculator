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
        radius = input("What is the radius of the circle? If you don't know radius type 0 >> ")
        if radius > 0:
            area = math.pi * (radius*radius)
            print "The area of this circle is %i%s squared" % (area, units)
        else:
            diameter = input("Please enter the diameter of the circle >> ")
            area = (math.pi/4) * (diameter * diameter)
            print "The area of this circle is %i%s squared" % (area, units)
    elif shape == 3:
        print "You have chosen a Triangle"
        print "I will now ask for some dimensions and units of measure"
        units = raw_input("What is the unit of measure? e.g. cm, m, inches etc... >> ")
        base = input("What is the length of the base of the Triangle? >> ")
        height = input("What is the height of the triangle? >> ")
        area = 0.5 * (base * height)
        print "The area of the Triangle is %i%s squared" % (area, units)

action(user_shape)
