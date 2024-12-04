def validate_alpha_input(prompt):
    while True:
        user_input = input(prompt).capitalize()
        if user_input.isalpha():
            return user_input
        print("Invalid input. Please enter alphabetic characters only.")

def validate_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please enter numeric values only.")

def validate_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please select a valid option.")