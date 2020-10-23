from microbit import *
import random
display.scroll("Steen Papier Schaar")

#een lijst maken met de vormen van de afbeeldingen
shapes=[Image("09990:99999:99999:99999:09990"), #Steen
Image("99999:90009:90009:90009:99999"), #papier
Image("90009:09090:00900:09090:90009"), #Schaar
Image("99099:99099:00000:09990:90009")] #Sad face

while True:
    gesture = accelerometer.current_gesture() # zet de variable gesture naar de huidige gesture huidige gesture
    if gesture == "shake": # zorgt ervoor dat je de microbit kan schudden
        display.show(random.choice(shapes)) # laat een random shape zien
