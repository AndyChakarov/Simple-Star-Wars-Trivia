import math
import string
import random

print("Simple Star Wars quiz. (SPOILERS!!!) Made by Andy Chakarov.")
cor1 = "Anakin Skywalker" #What other name does Darth Vader go by? (hint: he said that it doesnt mean anything to him anymore in episode 6 Return of the Jedi)
cor2 = "Ben Solo" #What was the original name of Kylo Ren?
cor3 = "Death Star" #What was the ultimate weapon that was rebuilt 3 times
cor4 = "Princess Leia" #Who was the jedi that was never seen on missions with lightsabers or use the force in a combat style?
cor5 = "Chewbaca" #What is the name of the character that has seen over 5 jedi?
cor6 = "bb-8" #What is the name of the orange-white droid introduced in The Force Awakens?
cor7 = "Yoda" #Who is the character that lived the longest?
cor8 = "Darth Vader" #Who at one point had the nickname "The Galaxy's doom"?
cor9 = "Han Solo" #Who somehow appeared as a ghost infront of Kylo Ren even when he wasn't a jedi and didn't use the force?
cor10 = "Padme Amidala" #Who is the mother of Luke Skywalker and princess Leia Skywalker
wrong = 0


g1 = input("What other name does Darth Vader go by? (hint: he said that it doesnt mean anything to him anymore in episode 6 Return of the Jedi): ")
if g1 == cor1:
     print("Congratulations! You got the answer right!")
else:
    print("That's not true!")
    wrong =+ 1

g2 = input("What was the original name of Kylo Ren?: ")
if g2 == cor2:
     print("Congratulations! You got the answer right!")
else:
    print("That's not true!")
    wrong += 1

g3 = input("What was the ultimate weapon that was rebuilt 3 times?: ")
if g3 == cor3:
    print("Congratulations! You got the answer right!")
else:
    print("That's not true!")
    wrong += 1

g4 = input("Who was the jedi that was never seen on missions with lightsabers or use the force in a combat style?: ")
if g4 == cor4:
    print("Congratulations! You got the question right!")
else:
    print("That's not true!")
    wrong += 1

g5 = input("What is the name of the character that has seen over 5 jedi?: ")
if g5 == cor5:
    print("Congratulations! You got the question right!")
else:
    print("That's not true!")
    wrong += 1

g6 = input("#What is the name of the orange-white droid introduced in The Force Awakens?: ")
if g6 == cor6:
    print("Congratulations! You got the question right!")
else:
    print("That's not true!")
    wrong += 1

g7 = input("Who is the character that lived the longest?: ")
if g7 == cor7:
    print("Congratulations! You got the question right!")

else:
    print("That's not true!")
    wrong += 1

g8 = input("Who at one point had the name The Galaxy's doom?: ")
if g8 == cor8:
    print("Congratulations! You got the answer right!")
else:
    print("That's not true!")
    wrong += 1

g9 = input("Who somehow appeared as a ghost infront of Kylo Ren even when he wasn't a jedi and didn't use the force?: ")
if g9 == cor9:
    print("Congratulations! You got the question right!")
else:
    print("That's not true!")
    wrong += 1

g10 = input("Who is the mother of Luke Skywalker and princess Leia Skywalker?: ")
if g10 == cor10:
    print("Congratulations! You got the answer right!")
else:
    print("That's not true!")
    wrong += 1

print("The quiz is over! You got", wrong, "answer/s wrong out of 10!")