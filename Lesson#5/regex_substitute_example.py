import re
def regex_substitute_example():
    text = "The color is red, but it could also be blue or green."
    pattern = r"red|blue|green"
    replaced_text = re.sub(pattern, "COLOR", text)
    print("Текст после замены:", replaced_text)

regex_substitute_example()