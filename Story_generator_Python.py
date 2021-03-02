

# Challenge One (Input and String Formatting)
# You and a partner will try to use your knowledge of Python to create a MadLib function.

# HOW-TO: Create a multi-line string variable called my_story which contains a short story about an animal in a specific borough of New York, performing some action involving one specific type of food.

# TODO: Ask the user through the command line for their picks for 'animal', 'borough', 'action' and 'food'

# TODO: Create a Python program that swaps those items in your story

# TODO: Print the user's story to the command line'''

#====================================================================================================

print("Welcome to the story generator")

animal = input("What's your favorite animal?\n")
borough = input("Which borough do you live in, or what's your favorite one, if you don't live in NYC?\n")
action = input("What's your favorite activity at dinner time?\n")
food = input("What's your favorite food?\n")

storyTemplate = "There's an {0} from {1} going to {2} and then going to eat some {3}".format(animal, borough, action, food)

print(storyTemplate)

    
