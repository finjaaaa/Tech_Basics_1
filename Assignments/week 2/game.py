#Assignment version one
import time
import sys

def typing_print(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Start
typing_print("Welcome to the quiz.")
time.sleep(1)
time.sleep(1)
player_name = input("Please enter your name: ")
print("Hi", player_name)
time.sleep(1)
typing_print("This quiz will find your perfect holiday destination. Have fun, " + player_name + "!")

# point system
points_norway = 0
points_la = 0
points_carribean = 0

#Question 1
typing_print("\nSo, first question...")
time.sleep(1)
time.sleep(2)
while True:
    landscape_type = str(input("Do you prefer mountains or sea? 🏔️ vs. 🌊: "))
    if landscape_type == "mountains":
        points_norway += 1
        points_la += 1
        typing_print("Interesting choice.")
        break
    elif landscape_type == "sea":
        points_carribean += 1
        points_la += 1
        typing_print("You seem like a water person!")
        break
    else:
        typing_print("Invalid answer. Please type 'mountains' or 'sea'.☺️")

#Question 2
typing_print ("Okay, second question coming up...")
time.sleep(1)
time.sleep(2)
while True:
    activity_type = str(input("Do you prefer active or relaxing holidays? (active/relaxing):"))
    if activity_type == "active":
        points_norway += 1
        typing_print("Adventure time!")
        break
    elif activity_type == "relaxing":
        points_carribean += 1
        typing_print("Chill mode activated!")
        break
    else:
        typing_print("Invalid answer. Please type 'active' or 'relaxing'.☺️")

#Question 3
typing_print ("I feel like I start to get a taste of your perfect holiday. But to really decide what fit's you well, I need to ask you some more questions... So here is the third question for you.")
time.sleep(1)
time.sleep(2)
time.sleep(3)
while True:
    daytime = str(input("Prefer daytime activities or nightlife? (daytime/nightlife): "))
    if daytime == "daytime":
        points_norway += 1
        typing_print("Early bird!")
        break
    elif daytime == "nightlife":
        points_la += 1
        typing_print("🎶Party time!")
        break
    else:
        typing_print("Invalid answer. Please type 'daytime' or 'nightlife'.☺️")

#Question 4
typing_print ("You've made some great decisions so far. Seems like your perfect holiday comes more and more within reach...")
time.sleep(1)
time.sleep(2)
time.sleep(3)
while True:
    temperature_type = str(input( "Do you want to spend your trip in a rather hot, mild or cold climate?:"))
    if temperature_type == "hot":
        points_carribean += 1
        print ("You enjoy the heat, i see", player_name)
    elif temperature_type == "mild":
        points_la += 1
        print("Not too warm, not too cold - always a great choice", player_name)
    elif temperature_type == "cold":
        points_norway += 1
        print("Nice decision,", player_name)
    else:
        typing_print("Your answer is invalid. Please chose between 'hot', 'mild' or 'cold' 😊")

#Question 5
typing_print ("We're halfway through the quiz already. This quiz went by rather fast, so far. Don't you think? So the last five questions are coming up and you're one step closer to your summer vacation. ☀️😎" )
time.sleep(1)
time.sleep(2)
time.sleep(3)
while True:
    hobby_type = str(input( "If you had to choose between 'nature', 'culture' or 'shopping'... What would your go-to-activity be for the trip?: "))
    if hobby_type == "nature":
        points_norway += 1
        typing_print ("Interesting choice.")
    elif hobby_type == "culture":
        points_carribean += 1
        typing_print("I bet you enjoy a good walk around museums. 😂")
    elif hobby_type == "shopping":
        points_la += 1
        typing_print("Nothing rounds up a holiday like a good souvenir, am I right?")
    else:
        typing_print("Your answer is invalid. Please chose between 'nature', 'culture' or 'shopping' 😊")

#Question 6
typing_print ("Question number 6 for you:")
time.sleep(1)
time.sleep(2)
time.sleep(3)
while True:
    lodging_type = str(input( "Would you rather stay in a holiday home, a resort or in a hotel when on vacation?:"))
    if lodging_type == "holiday home":
        points_norway += 1
        typing_print ("Nice decision. You enjoy having some private space.")
    elif lodging_type == "resort":
        points_carribean += 1
        print("Sound like the perfection decision for a stress-free vacay.")
    elif lodging_type == "hotel":
        points_la += 1
        print("Can't go wrong with a hotel.")
    else:
        typing_print("Your answer is invalid. Please chose between 'holiday home', 'resort' or 'hotel' 😊")

#Question 7
typing_print ("Qkay, next question.")
time.sleep(1)
time.sleep(2)
time.sleep(3)
while True:
    group_type = str(input( "Do you plan on travelling alone, with friends or with family?:"))
    if group_type == "alone" or group_type == "friends" or group_type == "family":
        if group_type == "alone":
            points_la += 1
        if group_type == "friends":
            points_norway += 1
        if group_type == "family":
            points_carribean += 1
        typing_print ("Thanks, I'll calculate it into my answer.")
    else:
        typing_print("Your answer is invalid. Please chose between 'alone', 'friends' or 'family' 😊")

#Question 8
print("I've got only two questions left for you,", player_name)
time.sleep(1)
time.sleep(2)
time.sleep(3)
duration_type = int(input("How long should your holiday be? Please choose a number between 2 and 21 days: "))
while True:
    try:
        duration_type = int(input("How long should your holiday be? Please choose a number between 2 and 21 days: "))
        if 2 <= duration_type <= 21:
            break  # Gültige Eingabe, Schleife verlassen
        else:
            typing_print("Your answer is invalid. Please choose between 2 and 21 days.")
    except ValueError:
        typing_print("Please enter a valid number.")

if 2 <= duration_type <= 5:
    points_la += 1
if 6 <= duration_type <= 14:
    points_carribean += 1
    points_norway += 1
if 15 <= duration_type <= 21:
    points_norway += 1


#Question 10
typing_print("Final question.😁")
time.sleep(1)
time.sleep(2)
time.sleep(3)
while True:
    transport_type = str(input( "What's your preferred type of transport on vacation? Do you prefer travelling by train, car or boat?:"))
    if transport_type == "train":
        points_norway += 1
        typing_print ("So you enjoy relaxing train rides with a view...")
    elif lodging_type == "car":
        points_la += 1
        typing_print("Perfect for spontaneous trips around the local area.")
    elif lodging_type == "boat":
        points_carribean += 1
        typing_print("Great choice to enjoy the sea. 🌊")
    else:
        typing_print("Your answer is invalid. Please chose between 'train', 'car' or 'boat' 😊")

#final answers
time.sleep(1)
time.sleep(2)
time.sleep(3)
time.sleep(4)
print("Hurray, you've made it through the quiz...😊 It's time to find out about your perfect holiday destination for this summer,", player_name)
time.sleep(1)
time.sleep(2)
print("\nCalculating your perfect destination...")
time.sleep(1)
time.sleep(2)
if points_norway > points_la and points_norway > points_carribean:
    typing_print("Your perfect destination is: NORWAY! 🏔️ You love a calm holiday trip while enjoying the beautiful nature. The colder weather is perfect for you to cool down during the usual summer heat.")
elif points_la > points_norway and points_la > points_carribean:
    typing_print("Your perfect destination is: LOS ANGELES! 🌆 A eventful city trip fits you perfectly. You enjoy the warm weather either at the beach or in the mountains. A large variety of fun activites is waiting for you.")
elif points_carribean > points_norway and points_carribean > points_la:
    typing_print("Your perfect destination is: THE CARRIBEAN! 🏝️ You love having a good and relaxing time at the beach with the sea always within reach. No matter if you wanna go surfing, snorkeling or just enjoy your drink and a good book in the sun - the decision is yours!")
else:
    typing_print("You are open for anything! All three destinations would be great for you. Either NORWAY! 🏔️, LOS ANGELES! 🌆 or THE CARRIBEAN! 🏝️")













