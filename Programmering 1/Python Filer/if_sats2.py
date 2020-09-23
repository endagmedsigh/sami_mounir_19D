#%%
import random as rnd 
poäng = rnd.randint(0,65)


klass = ["Sami", "Elev2","Tommy","Random"]


if (poäng > 60):
    betyg = "A"
elif (poäng >= 56):
    betyg = "B"
elif (poäng >= 51):
    betyg = "C"
elif (poäng >= 41):
    betyg ="D"
elif (poäng >= 31):
    betyg ="E"
else:
    betyg ="F"
#slumpvis väljer ett elemnti listan klass
elev =rnd.choice(klass)

print(f"Eleven {elev} fick {poäng} poäng vilket ger betyget {betyg}")

#%%
s=0
for i in range(1,10000):
    s += i

print(s)