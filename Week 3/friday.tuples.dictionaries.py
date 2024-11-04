# Tuples kortezhi the list that can not be changed
# Created by using () and elements divided by ,

ticket_info = ("Darkhan", "Place 3", "Time 19:00")
#When ticket is bought, place is secured and can not be changed

#Advantages
#1) Speed: быстрее обработка
#2) Less storage taker

#Dictionary - it hold KEY + VALUE
#is created using the figurative paranthesis {"key":"value", "key":"value"}
# we can derive the elements as it is in the list
# Old phone book
# In the contact list for example, we use name of the person and their number is in there as value

phone_book = {
    "Bekzat": "+77053876883",
    "Bobik": "+8 8893 76643",
    "Oleg": int(),
    "Oleg1": str(),
}

#key and the value can be of any data types
# Why? In order to find the specific data based on the key information
# Excel is also based on KEY + VALUE
# Each of the cell has its own name

excel_sheet = {
    "A1": 333,
    "A2": 444,
}

# How to retrieve the value, we do that by using the key
number_bekzat = phone_book["Bekzat"]

#How to add new contact, new value
phone_book["Alex"] = "+1234567890"
print(phone_book)

#Update the currect contact
phone_book["Bekzat"] =  "+77053876884"
print(phone_book)

# WE CAN'T CREATE TWO KEYS WITH THE SAME NAME
# There can be dictionaries in the dictionary
# Outer dictionary
outer_dict = {
    "person1": {
        "name": "Alice",
        "age": 25
    },
    "person2": {
        "name": "Bob",
        "age": 30
    }
}

# Both inner dictionaries have the same keys ("name" and "age")
print(outer_dict)
# Accessing nested dictionary values
print(outer_dict["person1"]["name"])  # Output: Alice
print(outer_dict["person2"]["age"])   # Output: 30


# Delete using the key
del phone_book["Bobik"]
print(phone_book)

# if we just wanted to return some value, the absence of the key will return error
# If there is no key, we can skip the error by using the GET:

number = phone_book.get("Ivan", "Contact is not found")
print(number) # Result if Contact is not found

#We can use for loop in dictionary, using their key + value:

for name, numbers in phone_book.items():
    print(f"{name}: {numbers}")
    print(f"This is the name of the contact {name}")
    print(f"This is the phone number of our client {str(numbers)}")

# Methods in dictionary
# items() = retrieves a couple key + value
print(phone_book.items()) # tuples are for speed

# keys() - only keys
print(phone_book.keys())
list_of_keys = list(phone_book.keys())
print(list_of_keys)

# values() - only values
print(phone_book.values())

# pop(key) - deletes element using their key and returns the value
removed_number = phone_book.pop("Alex") # necessarily key to be written
print(removed_number)
# Вывод: "+1234567890"
print(phone_book)

#clear() - очищает весь словарь
phone_book.clear()
print(phone_book)
# Output: {}
