movies = ["Naa", "AAAA", "BBBB", "Baa", "Faa"]

for i in movies:
    if (i.find("aa") != -1):
        print(i)
        print(i.find("aa"))
    else:
        continue

# Splitting the  text using the specific character

text = "apple,banana,pear"

print(text.split(",")) # and it returns as list ['apple', 'banana', 'pear']

# Обьединение списка в строку - using JOIN

list_of_fruits = ['apple', 'banana','cherry']

string_of_fruits = ', '.join(list_of_fruits) # Just returns string value
print(string_of_fruits) # Output is "apple, banana, cherry"

# MAX and MIN takes out the maximum and minumum value in the list

salaries_in_thousands = [1000, 300, 700, 350]
max_numbers = salaries_in_thousands[0]
for i in salaries_in_thousands:
    if max_numbers >= i:
        max_numbers = i

print(max_numbers)

# List of numbers
numbers = [3, 7, 2, 9, 4, 6]

# Initialize the maximum value to the first element in the list
max_value = numbers[0]

# Loop through the list to find the maximum value
for num in numbers:
    if num > max_value:
        max_value = num

# Output the maximum value
print(f"The maximum value is: {max_value}")

print(max(salaries_in_thousands))
print(min(salaries_in_thousands))

# Formatting the strings
name = "Ivan"
age = 30
message = "My name is " + name + ", and I am " + str(age) + " years old"
print(message)

name1 = "Ivan"
age1 = 30
message1 = "My name is {}, and I am {} years old.".format(name1, age1)
print(message1)

# Using f before the strings will help you do that
name2 = "Ivan"
age2 = 30
message2 = f"My name is {name2}, and I am {age2} years old"
print(message2)

username = "Alexey"
score = 150
print(f"Congratulations, {username}! You scored {score})")

username1 = input("Enter you name: ")
message3 = f"Hello {username1}, you reached our system, stay back and be quiet!"
print(message3)