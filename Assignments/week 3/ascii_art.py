import random
import time

# Instructions for the user
print("Welcome to the ASCII Art Generator!")
print("You'll be asked for:")
print("- Width (integer, 5 to 20)")
print("- Height (integer, 3 to 10)")
print("- Your favorite character (just one, e.g. *, #, @, etc.)")

# Get user inputs with validation
while True:
    try:
        width = int(input("Enter width (5-20): "))
        if 5 <= width <= 20:
            break
        else:
            print("Please enter a number between 5 and 20.")
    except ValueError:
        print("That's not a valid number.")

while True:
    try:
        height = int(input("Enter height (3-10): "))
        if 3 <= height <= 10:
            break
        else:
            print("Please enter a number between 3 and 10.")
    except ValueError:
        print("That's not a valid number.")

while True:
    char = input("Enter a single character to use: ")
    if len(char) == 1:
        break
    else:
        print("Please enter exactly one character.")

# List of random filler characters
filler_chars = ['.', '*', '+', '@', '#', '%', '&']

print("\nGenerating your ASCII art...\n")
time.sleep(1)

# Nested loops to build the ASCII art
for row in range(height):
    line = ""
    for col in range(width):
        # Randomly decide to use user's char or a random filler
        if random.random() < 0.6:  # 60% chance to use user's char
            line += char
        else:
            line += random.choice(filler_chars)
    print(line)
    time.sleep(0.3)  # Animation effect

# Bonus: Unexpected message
if char == "*":
    print("\nYou chose the classic star! 🌟")
elif char == "@":
    print("\nAt your service! 😉")
else:
    print("\nASCII art complete! Hope you enjoyed the randomness!")
