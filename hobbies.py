"""Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies."""
hobbies = []

# Add your code below!
for i in range(3):
    hobby = input("Enter your hobby: ")
    print (hobby)
    hobbies.append(hobby)
    i += 1