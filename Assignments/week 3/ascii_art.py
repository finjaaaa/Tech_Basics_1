import random
import time

print("🌴 ASCII-Island-Generator 🌴")
print("Please enter the size of your island and a symbol.")

# while-loop for the size
while True:
    try:
        width = int(input("width of the island (7-30): "))
        if 7 <= width <= 30: break
        print("Please enter a valid width between 7 and 30!")
    except:
        print("unvalid number!")

while True:
    try:
        height = int(input("height of the island (4-20): "))
        if 4 <= height <= 20: break
        print("Please enter a valid height between 4 and 20!")
    except:
        print("unvalid number!")

while True:
    island_symbol = input("Which symbol dou you want for the island? (one symbol only.): ")
    if len(island_symbol) == 1: break
    print("Please enter one symbol only!")

water = "~"
edge = [" ", water]

print("\nGenerating your island...\n")
time.sleep(1)

# centre of the island
centre_x = width // 2
centre_y = height // 2
max_radius = min(width, height) // 2

for y in range(height):
    line = ""
    for x in range(width):
        # length from the centre, random for an irregular island shape
        space = ((x - centre_x) ** 2 + (y - centre_y) ** 2) ** 0.5
        border = max_radius - random.randint(0, 2)
        if space < border:
            # possibility for a sand beach ('.')
            if random.random() < 0.12:
                line += "."
            else:
                line += island_symbol
        else:
            # water or empty edge
            line += random.choice(edge)
    print(line)
    time.sleep(0.20)

print("\nThe island is ready for an adventure!\n")

