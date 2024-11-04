# Loops - циклы (повторение действий)
# while 
# for 

# x = 1
# while x<3:
#     print(x, end=", ")
#     x = x + 1
# print("\nEnd of loop ", x)

# str = 'Hello' # H is indexed as 0, then 1 2 the ends at 4
# l = len(str)

# for a in str:
#     print(a)

# for a in range(l):
#     print(str[a])

# str = 'Madiyar' # H is indexed as 0, then 1 2 the ends at 4
# l = len(str)

# M is 0
# a is 1
# d is 2
# i is 3
# y is 4
# a is 5
# r is 6

# for a in range(2, l, 2): # range(starting_index, end, steps)
#     print(str[a])

# a = 0
# for i in str:
#     print(f'{i} is {a}')
#     a += 1
# x=5 
# while x<=30:
#     if x == 10:
#         x+=5
#         continue
#     print(x)
#     x+=5

# print('Loop ended', x)

# while x<30:
#     j=x
#     while j<15:
#         if j==10:
#             break
#         print('Second loop j is', j)
#         j+=5
#     print('first loop x is', x)
#     x+=3
# print('Loop ended x is ', x)

# Task 1 do not show the letter "a"
# word = "Congratulations"

# for i in word:
#     if i in "a":
#         continue
#     print(i, end="")

# Task 2 do not show the index 5 and 7 
# word = "Congratulations"
# length = len(word)
# for i in range(length):
#     if i==5 or i==7:
#         continue
#     print(word[i], end="")

x= 30
if x%3==0:
    print("x is divisible by 3")
if x%2==0:
    print("x is even")
if x%2!=0:
    print("x is odd")

