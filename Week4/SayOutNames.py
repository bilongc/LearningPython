# Program on book page 63
# Ask the user for their name
name = input("What is your name?")

# Keep printing names until we want to quit
while name != "":
    # Print their name 10 times
    for x in range(10):
        # Print their name followed by a space, not a new line
        print(name, end = " ")
    print()
    # Ask for another name, or quit
    name = input("Type another name, or just hit [ENTER] to quit: ")
print("Thanks for playing!")
