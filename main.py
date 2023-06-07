import math

name = input("What's your name?:" )
num1 = float(input("Hello, " + name + " Please enter first number: "))
num2 = float(input("Thanks!, now enter the second number: "))
operator = input("Thanks!, now choose the operator (+/-/*/%): ")

if operator == "+":
    print ("Numbers added to each other give a result: ", (num1+num2))
elif operator == "-":
    print ("Numbers subtracted give a result: ", num1-num2)
elif operator == "*":
    print ("Numbers multiplied give a result: ", num1*num2)
elif operator == "%":
    print ("Numbers divided give a result: ", num1/num2)
