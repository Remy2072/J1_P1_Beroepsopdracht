from microbit import *
import random
import speech

lengteWoordArray = 3

onderwerp = ["Remy", "Mike", "Suzan"]
werkwoord = ["aait", "loopt", "leest"]
rest = ["kat", "werk", "boek"]



def sayTheWords1(word): 
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)
    
def sayTheWords2():
    willeKeurigGetal = random.randint(0, lengteWoordArray - 1)
    sayTheWords1(onderwerp[willeKeurigGetal])
    sayTheWords1(werkwoord[willeKeurigGetal])
    sayTheWords1(rest[willeKeurigGetal])

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sayTheWords1("hello i am happy")
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sayTheWords1("why are you sad")
    elif display.read_light_level() < 40:
        sayTheWords2()
    else:
        display.show(Image.SQUARE)
