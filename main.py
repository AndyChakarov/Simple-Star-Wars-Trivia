import math
import string
import random

print("Simple Star Wars quiz. (SPOILERS!!!) Made by Andy Chakarov.")
cor1 = "Anakin Skywalker" #What other name does Darth Vader go by? (hint: he said that it doesnt mean anything to him anymore in episode 6 Return of the Jedi)
cor2 = "Ben Solo" #What was the original name of Kylo Ren?
cor3 = "Death Star" #What was the ultimate weapon that was rebuilt 3 times
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

print("The quiz is over! You got", wrong, "answers out of 3!")