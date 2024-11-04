# Let's calcualte the quantity of week
# number_of_weeks = 0
# total_days = 365
# step = 7
# for i in range(total_days, 0, -step):
#     print(i)
#     number_of_weeks += 1
#     print(number_of_weeks)
#
#
# print(number_of_weeks)
#
# for random in range(10, 2):
#     print("What")

# number_of_weeks = 0
# total_days = 365
# step = 7
# while total_days>=0:
#     print(number_of_weeks)
#     number_of_weeks += 1
#     total_days -= step
#     print(total_days)

# day_time = "morning"
# am_i_hungry = True
#
# if day_time == "morning":
#         #? если это УТРО и если я ГОЛОДЕН
#         print('КУШАТЬ НАДАААА, завтракаем')
#     else:
#         #? если это УТРО, но я НЕ ГОЛОДЕН
#         print('Утро, но я не голоден')
#
# if (day_time == ' morning') and (am_i_hungry == True):
#     print('asdf')

# Homework
# 1  Используя условия (if-else-elif), напишите все четные числа от 1 до 100

for i in range(1, 101):
    if i%2==0:
        print(i, end=" ")

print()

for i in range(1, 101, 2):
    print(i, end=" ")