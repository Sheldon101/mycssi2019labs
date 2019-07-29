#num1=int(raw_input("Enter num #1:"))
#num2=int(raw_input("Enter num #2:"))
#total= num1 + num2
#print("The sum is: "+ str(total))
# need to be a string so computer can read it
# all strings can be integers but not all integers can be strings
# num = int(raw_input("Enter a number:"))
# if num>0:
#     print("That's a postive num!")
# elif num<0:
#     print("That's a negative num!")
# else:
#     print("Zero is neither postive nor negative!")
# string = "hello"
# for letter in string:
#     print(letter.upper())
#
# for i in range(5): repaeted executed depend on how may letters in the string so hello would be 5
#     print(i)
#
# x=1
# while x <=5:
#     print(x)
#     x=x+1

# my_name= "B"
# friend1= "A"
# friend2= "J"
# friend3= "M"
# print(
# "My name is %s and my friends are %s, %s, and %s" %
# (my_name,friend1,friend2,friend3 )
# )
#
# name= "C"
# age= 19
# print("My name is "+ name + "and I'm " + str(age)+"years old.") one way
# print("My name is %s and I'm %s years old." %(name,age)) second way

# def greetAgent():
#     print("B. James Bond.")
# greetAgent() always call the func
#
# def greetAgent(first_name, last_name):
#     print("%s. %s. %s." % (last_name, first_name, last_name))
# One way
#
#
# def createAgentGreeting(first_name, last_name):
#     return"%s. %s. %s." % (last_name, first_name, last_name)
#
# print(createAgentGreeting("Citlally", "G"))
# second way
word = "computerz"
print(word[:5])  # prints "compu"
print(word[:-1])  # prints "computer"
print(word[4:])  # prints "uterz"
print(word[-3:])  # prints "erz"
