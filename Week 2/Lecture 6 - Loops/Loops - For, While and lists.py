#? For
#* I bet with my friend, that I can write "BMW is better than Audi"
# -- 99 times, like a programmer, I will not repeat the same
# manually 99 times, I will Use "For"

# Example #1

# how_many_times = 99
# fraza = "BMW is better than Audi"
#
# # We use range to define the quantity of iteration
#
# for line_number in range(how_many_times):
#     print(fraza)
#     print(line_number)

#While loops
# I want to buy coffee, till I go broke

# money_i_have = 5000
# coffee_price = 1200
# how_many_coffee = 0
#
# while money_i_have>=coffee_price:
#     print(money_i_have)
#     print("I bought coffee, it means I paid 1200")
#     money_i_have = money_i_have - coffee_price
#     how_many_coffee=how_many_coffee+1
#     print(money_i_have)
#     print(how_many_coffee)
#
# # These lines will be executed after the the loop is finished
# print("I don't have money anymore")
# print("Money left: " + str(money_i_have))
# print("How many coffees I bought: " + str(how_many_coffee))

# Let's explore the whole power of range
# range(start, finish, the step)

# Example: Imagine, you have a charger, that charges you phone
# If you want to check the battery level every 15 mins for the next 2 hours
# you can use the range as following:

# check = 15
# overall_time = 121 # convert hours to minutes + 1, so 120th minute will be included
#
# for check_time in range(0,overall_time,check):
#     print("It's time to check, 15 mins passed")
#     print(check_time)







