# храним нам нужные данные разного вида сразу
# Function is feeding the cat,

# Cat has something himself to do that is
# Feed(cat), here cat is the argument

# Method is something that cat can do, works as we command it to the line

# like cat.purr()

# Concatination
name = "Darkhan"
full_name= "Mashirapov " + name
print(full_name)

# To derive some part of the strings
message = "I am learning programming"
print(message[2:13]) # space, punctuation counts

# Deriving works like range(start, finish(inclusive), step)

# We can capitilise, make it upper, lower case
print(message.upper())
print(message.lower())
print(message.capitalize()) #Only the 0th indexed value will be capitilised
print(message[0:7].upper()) # we can't write something into paranthesis ()
print(message.title()) # every word is capitilised
print(message.replace("I am", "We are")) #replace even if it is part of the word

fraza = "Я учусь я программироватья! я это круто"
print(fraza.replace("я", "We", 2)) # 2 means maximum number of changes it means that the last я will not be changed

# Functions we use on the strings
print(len('01234abcd')) #space and punctuation and anything in the line is counted

# there is 0
# there is null

# Function str, transforms,  turns into string
print(str(999))
print(int("999"))
print(float(999))

# lists
# we create them by using the square brackets
text = "I am cool"
chislo = 667
# This is list - not array
tasks = [text, "to wake up at 6 am", "go to the gym at 6.30 am", chislo, [1,3,5]]
# we can create list bu using just list()
print(tasks[0][0]) # first list is indexed as first number, then it goes for the first 0 of the 0 in the list
print(tasks[4][1]) # fourth element of the first list, and the first element of the fourth element of the list

# to add element of the list to the end
tasks.append("Go to the gym at 6:30")
print(tasks)

# To add element to the index we want
tasks.insert(1, "To drink a coffee")
print(tasks)

#To derive the certain element of the list using their index
print(tasks[1]) # if the index is higher than the length, insert adds it to the end


# books = []
#
# while len(books)<3:
#     books.append(input("Input your book: "))
# # extend learn, we add list as independent elements
#
# print(books)

# input returns everything as string
# email = input('Inout your email: ')
# print(email.lower())

# To remove it is just tasks.remove()

tasks.extend(["sjafkjdfk", "dnasjkfnjkd", "sakfjklsf"])
print(tasks)
# when we use extend, they are added as new objects rather than list  in the list
# we also can use the name of the list, so elements of the new list is added to new list
# operator
books = ["Harry potter"]
tasks.insert(1, books)
print(tasks) # separately after function, but here books will be as new list in the old list



# Homework calculator
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# choice = input("What operation do you want to choose? ")
# print("Select operation:")
# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
#
# if int(choice)==1:
#     c = a + b
#     print(f"Sum of {a} and {b} is: " + str(c) )
# elif int(choice)==2:
#     d = a - b
#     print(f"Difference of {a} and {b} is: " + str(d))
# elif int(choice)==3:
#     e = a * b
#     print(f"Product of {a} and {b} is: " + str(e))
# elif int(choice)==4:
#     f = a / b
#     print(f"Product of {a} and {b} is: " + str(f))

# We can't remove by identically saying the word, remove for example
# Also we use index to remove particular element in the list
tasks.remove("sjafkjdfk")
tasks.pop()  # pop deleted the last element last element on the
# we can also assign the value to variable

last_deleted_element = tasks.pop() # so it basically removes and assignmet the last element to a new variable
print(tasks)

# deleting by index in the list
del tasks[1] #just python instrument that will help you to delete the index

# clear just cleans the list and makes it empty
tasks.clear()

# Sorting the elements in the list in ascending order
numbers = [5, 2, 10, 7, 3, 1, 1, 0]
numbers.sort()
print(numbers)

# when numbers and the letters
numbers_and_letters = [99, 55, 1, True, False, 3.3, 0]
numbers_and_letters.sort()
print(numbers_and_letters)
# so when sort for string is alphabetical for number it is ascending order, punctuation goes first, ASKI
# so capital letters go first

# sorted() - function that just a sorted way and it created copy sorted, and do not change the original
unsorted_tasks = ['Sleep', "Eat", "Run"]
sorted_tasks = sorted(unsorted_tasks)
print(sorted_tasks)

# Перебор элементов в семье
# for - позволяет перебирать все элементы списка
# movies = ["NNNN", "AAAA", "BBBB"]
#
# for movie in movies:
#     print(movie)
#
# for element in range(0, len(movies)):
#     movie = movies[element]

movies = ["Naa", "AAAA", "BBBB", "Baa", "Faa"]

for i in movies:
    if i in "aa":
        print(i)
    else:
        continue



