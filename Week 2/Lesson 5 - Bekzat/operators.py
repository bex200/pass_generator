# Operators - действие над данными 

#* Arithmetic 
# Whole division (//) - divide and leave the whole number
# % remainder - divide and find the remainder

# example of addition

product_name = "Asus Vivobook 16x"
description = " has a 16-inch display, with 16GB RAM and i5-13th gen"

product_sentence = product_name + description
print(product_sentence)

one_star = "*"
ten_stars = one_star*10
print(ten_stars)

# Example whole division 
pizza_boxes = 7 
people = 3 
pizza_boxes_per_person = pizza_boxes//people
print(pizza_boxes_per_person)

# Remainder
leftover_piza_boxes = pizza_boxes%people
print(leftover_piza_boxes) 

pizza_boxes = 10 
people = 5
leftover_pizza_boxes = pizza_boxes%people 
pizza_boxxes_per_person = pizza_boxes//people

# Сравнительные Операторы -- compare two values
# not equal != 
orange = 4
apples = 4 
bananas = 3

apples == bananas
apples > bananas
apples < bananas
orange <= apples

# Logical operators - conditions and equal, returns boolean values
# and = Both of them are TRUE?
# or = At least one of them is TRUE
# not = not true

is_shiny_today = True 
do_i_have_money = True 
will_i_go_outside = (is_shiny_today) and (do_i_have_money)

print(will_i_go_outside)

skolko_i_have_money = 4 
will_i_go_outside = skolko_i_have_money > 3 and is_shiny_today
print(will_i_go_outside)



