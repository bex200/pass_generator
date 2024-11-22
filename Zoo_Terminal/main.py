import constants as const
import utilities as util
import zoo_cl as zoo
import animal_cl as animal
import random


def add_exhibit(z):
    name = util.validate_alpha_input("Please, enter exhibit name: ")
    location = util.validate_alpha_input("Please, enter exhibit location: ")
    z.add_exhibit(name, location)
    print(f"Exhibit '{name}' at '{location}' added successfully.")


def add_staff(z):
    staff_type_key = util.validate_choice("1. Add a Zookeeper\n2. Add a Vet\n", const.STAFF_TYPES.keys())
    staff_type = const.STAFF_TYPES[staff_type_key]
    name = util.validate_alpha_input("Please, enter staff name: ")
    age = util.validate_numeric_input("Please, enter staff age: ")
    z.add_staff(staff_type, name, age)
    print(f"New {staff_type} '{name}' added successfully.")


def add_animal(z):
    if len(z.exhibits) < 1:
        print("No exhibits available. Add an exhibit first.")
        return

    name = util.validate_alpha_input("Please, enter animal name: ")
    age = util.validate_numeric_input("Please, enter animal age: ")

    print("Choose an exhibit (by ID):")
    for i, exhibit in enumerate(z.exhibits, start=1):
        print(f"\t{i}. {exhibit}")
    exhibit_index = util.validate_numeric_input("") - 1

    is_endangered = util.confirm_input("Is this animal endangered? (Y/N): ")

    print("Select an animal to add:")
    animals_to_add = {}

    for key, animals in const.ANIMAL_CLASSES.items():
        animals_to_add.setdefault(animals, []).append(key)

    for animals, keys in animals_to_add.items():
        readable_command = animals.capitalize()
        keys_display = ", ".join(keys)
        print(f"{readable_command}:\n  Type: {keys_display}")

    animal_key = util.validate_choice("", const.ANIMAL_CLASSES.keys())
    animal_class = getattr(animal, const.ANIMAL_CLASSES[animal_key])
    try:
        z.exhibits[exhibit_index].add_animal(animal_class(name, age, is_endangered))
        print(f"{animal_class.__name__} '{name}' added to exhibit '{z.exhibits[exhibit_index].name}'.")
    except Exception as e:
        print(f"Error adding animal: {e}")


def view_exhibits(z):
    print(f"Current {len(z.exhibits)} Exhibits:")
    for exhibit in z.exhibits:
        print(f"\t{exhibit}")


def view_staff(z):
    print(f"Current {len(z.staff)} Staff:")
    for staff in z.staff:
        print(f"\t{staff}")


def view_animals(z):
    if not z.exhibits:
        print("No exhibits available.")
        return

    total_animals = sum(len(exhibit.animals) for exhibit in z.exhibits)
    print(f"All {total_animals} Animals in our Exhibits:")
    for exhibit in z.exhibits:
        print(f"{exhibit.name}:")
        if not exhibit.animals:
            print("\tNo animals in this exhibit.")
        else:
            for animal_exhibited in exhibit.animals:
                print(f"\t{animal_exhibited}")


def make_staff_do_task(z):
    if not z.staff:
        print("No staff members available.")
        return

    print("Select a staff member:")
    for i, staff in enumerate(z.staff, start=1):
        print(f"\t{i}. {staff.name} ({staff.position})")

    staff_index = util.validate_numeric_input("Enter the number of the staff: ") - 1
    staff_member = z.staff[staff_index]

    if staff_member.position.lower() == "zookeeper":
        print("1. Report\n2. Work\n3. Feed an Animal")
        choice = util.validate_choice("Choose a task: ", ["1", "2", "3"])
        if choice == "1":
            exhibit_index = z.select_exhibit()
            if exhibit_index is None:
                print("No exhibit selected. Operation canceled.")
            else:
                staff_member.report(exhibit_index)
        elif choice == "2":
            staff_member.work()
        elif choice == "3":
            print("Select an animal:")
            exhibited_animal_index = z.select_an_animal()
            if exhibited_animal_index is None:
                print("No animal selected. Operation canceled.")
            else:
                food = util.validate_alpha_input("Enter food for the animal: ")
                staff_member.feed(exhibited_animal_index, food)

    elif staff_member.position.lower() == "vet":
        print("1. Report\n2. Check Health of an Animal")
        choice = util.validate_choice("Choose a task: ", ["1", "2"])
        if choice == "1":
            exhibit_index = z.select_exhibit()
            if exhibit_index is None:
                print("No exhibit selected. Operation canceled.")
            else:
                staff_member.report(exhibit_index)

        elif choice == "2":
            print("Select an animal:")
            exhibited_animal_index = z.select_an_animal()
            if exhibited_animal_index is None:
                print("No animal selected. Operation canceled.")
            else:
                staff_member.check_health(exhibited_animal_index)

    else:
        print(f"{staff_member.position} cannot perform any specific tasks.")


def watch_animal_action(z):
    animal_w = z.select_an_animal()

    if animal_w is None:
        print("No animal selected. Operation canceled.")
        return

    animal_type = animal_w.species

    if animal_type in const.ANIMAL_ACTIONS:
        available_methods = [getattr(animal_w, action) for action in const.ANIMAL_ACTIONS[animal_type]]
        action = random.choice(available_methods)
        print(f"Watching {animal_w.name} the {animal_type} perform an action:")
        action()
    else:
        print(f"{animal_w.name} the {animal_type} has no specific actions defined.")


def perform_daily_operations(z):
    z.daily_operations()


def display_help():
    print("~-~-~-~-~ ZOO OS TERMINAL HELP ~-~-~-~-~")
    command_to_keys = {}

    for key, command in const.MENU_OPTIONS.items():
        command_to_keys.setdefault(command, []).append(key)

    for command, keys in command_to_keys.items():
        readable_command = command.replace('_', ' ').capitalize()
        keys_display = ", ".join(keys)
        print(f"{readable_command}:\n  Call: {keys_display}")


def main():
    z = zoo.Zoo()
    print("~-~-~-~-~ ZOO OS TERMINAL ~-~-~-~-~")
    print("~-~-~-~-~ HINT: USE HELP ~-~-~-~-~")

    while True:
        choice = util.validate_choice("TERMINAL##: ", const.MENU_OPTIONS.keys())
        command = const.MENU_OPTIONS[choice]

        if command == "add_exhibit":
            add_exhibit(z)
        elif command == "add_staff":
            add_staff(z)
        elif command == "add_animal":
            add_animal(z)
        elif command == "view_exhibits":
            view_exhibits(z)
        elif command == "view_staff":
            view_staff(z)
        elif command == "view_animals":
            view_animals(z)
        elif command == "staff_task":
            make_staff_do_task(z)
        elif command == "animal_action":
            watch_animal_action(z)
        elif command == "daily_operations":
            perform_daily_operations(z)
        elif command == "help":
            display_help()


main()
