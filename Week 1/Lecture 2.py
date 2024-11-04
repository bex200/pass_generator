# x=5.15
# j=-5
# b="Hello"
# c='Hello'
# d=True # 1
# e=False #0
# b=j//2 # only the integer

# + adds strings together 
# \n - new line 
# \t - tab 
# \' or \"  can be used одинарные 

# Conditional Operations 
# cmd + / make a line into a comment 

# x = 3
# if x>5:
#     print("x is more than 5")
# elif x==3:
#     print("x is 3")
# else:
#     print("x no more than 5")

# elif lines runs the first correct and ignored the rest 

# x = 3
# if x<5:
#     print("x is more than 5")
# if x==3:
#     print("x is 3")
# else:
#     print("x no more than 5")

# but if the ifs go one after another each if statement is checked

# x = 3

# if x>=3:
#     print("x bolshe ili ravmo 3")
# if x<=3:
#     print("x bolshe ili ravno 3")

# if x>3 or x==3:
#     print("Success")

# name = "Madiyar"

# if name == "Madiyar":
#     print("Hello " + name)

grade = int(input("Enter your grade: "))

if grade>0 and grade<=60:
    print("Your grade is 2")
elif grade>60 and grade<=80:
    print("Your grade is 3")
elif grade>80 and grade<=90:
    print("Your grade is 4")
else:
    print("Your grade is 5")



