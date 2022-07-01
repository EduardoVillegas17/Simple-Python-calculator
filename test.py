#single line comment
#another line

#variables
name="Eduardo"
last_name="Villegas"
age=23

print("Hi! Welcome "+name)

print("My age is: "+str(age))

#if statement
if age <100:
    print("No worries, you are still young!!")

elif age ==100:
        print("Wow! you to do a century")

else:
    print("Sorry, you are getting a little old now")

#Functions
def hello():
    print("Line1")
    print("Line2")
    print("Line3")
    print("Line4")


def say_hello():
    print("Hello there: ")

say_hello()

hello() #function call