# Load text banks
with open('BAD_DECISION/tasks.txt') as f:
    TASKS = f.read().splitlines()

with open('BAD_DECISION/satisfaction.txt') as f:
    SATISFACTION = f.read().splitlines()

with open('BAD_DECISION/health.txt') as f:
    HEALTH_STATUS = f.read().splitlines()

# Animals aliases
ANIMAL_CLASSES = {
    "1": "Lion",
    "lion": "Lion",
    "l": "Lion",
    "-l": "Lion",
    "2": "Monkey",
    "monkey": "Monkey",
    "m": "Monkey",
    "-m": "Monkey",
    "3": "Penguin",
    "penguin": "Penguin",
    "p": "Penguin",
    "-p": "Penguin"
}

ANIMAL_ACTIONS = {
    "Lion": ["sleep", "make_sound", "assert_dominance"],
    "Penguin": ["sleep", "make_sound", "swim"],
    "Monkey": ["sleep", "make_sound", "grapple_tricks"],
}

# Staff aliases
STAFF_TYPES = {
    "1": "Zookeeper",
    "zoo": "Zookeeper",
    "keeper": "Zookeeper",
    "zookeeper": "Zookeeper",
    "2": "Vet",
    "vet": "Vet",
    "v": "Vet"
}

# Menu commands                                     this is so much fun tbf
MENU_OPTIONS = {
    "1": "add_exhibit",
    "ae": "add_exhibit",
    "ea": "add_exhibit",
    "-ae": "add_exhibit",
    "-ea": "add_exhibit",
    "add exhibit": "add_exhibit",

    "2": "add_staff",
    "as": "add_staff",
    "sa": "add_staff",
    "-as": "add_staff",
    "-sa": "add_staff",
    "add staff": "add_staff",

    "3": "add_animal",
    "an": "add_animal",
    "na": "add_animal",
    "-an": "add_animal",
    "-na": "add_animal",
    "add animal": "add_animal",

    "4": "view_exhibits",
    "5": "view_staff",
    "6": "view_animals",
    "7": "staff_task",
    "8": "animal_action",
    "9": "daily_operations",
    "help": "help",
    "h": "help"
}
