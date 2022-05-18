myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print(myString , "is of the data type" , str(type(myString)))
#Concatenar cadenas
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print(str(type(thirdString)))
#Input
name = input("What is your name? ")
print(name)
#Encuesta
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
print(f"{name}, you like a {color} {animal}!")