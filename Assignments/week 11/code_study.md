### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)

I found the Code on GitHub (https://github.com/SaadARazzaq/Text-Adventure-Game/blob/main/game.py) and chose this one,
it might be helpful for my final project - which will probably also be pretty similar to a quest game.
---

1. What does the program do? What's the general structure of the program? 
The program is an adventure game where you choose your character, fight monsters, travel between places and complete
quests and collect items. It consists of a player and a monster class and a main class that's responsible for the
graphical surface and the game loop.
---

1. Function analysis: pick one function and analyze it in detail:

- What does this function do?
The function battle (self, monster) executes a fight between player and monster, decides the winner and returns a battle
log. 
- What are the inputs and outputs?
input: self - the current self-object; monster - a monster-object
output: tuple with 3 values - result ("Victory" or "Defeat"), battle log (text), conclusion (text) 
- How does it work (step by step)?
The function starts with an empty text-protocol (battle_log = "").
It executes a while-loop as long as the player is alive and the monster isn't defeated.
In every loop the player attacks, a random damage is calculated and subtracted from the monster-object. The result is
written into the battle log. If the monster isn't defeated it attacks the player, a random damage is calculated and 
substracted from the player defense and the player health reduced. The result is written into the battle log again.
If the player or the monster have no health points left the loop ends. It is then checked who won: if the player is
defeated, it's recorded in the log and the function returns "Defeat". If the monster is defeated, it's recorded in the
log and the functions returns "Victory". The log and a conclusion are also returned. 

---

1. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)
I learned what Tkinter is and it helped me to understand how i should structure the code for my final assigment and how 
to separate the game logic fromm the GUI.

1. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?
After reading the python and Tkinter documentation I was able to gain a better understanding of how the GUI is
connected from the game logic. 
---

Extra notes