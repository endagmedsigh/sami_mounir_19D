#%%
number = float(input("Skriv ditt nummer"))

if number == 0:
    print("Ditt nummer är 0") 
elif number > 0:
    print("Ditt nummer är positivt")
else:
    print("Ditt nummer är negativt")

#%%
number =float(input("Skriv ditt nummer"))

if number%5 == 0 and number%2 == 0:
    print("Ditt tal är både jämnt och delbart med 5")
elif number%5  == 0 and number%2 == 1:
    print("Båda udda och delbart med 5")
elif number%2 == 0:
    print("Ditt nummer är jämnt")
elif number%5 == 0:
    print("Ditt tal är delbart med 5")
else: 
    print("Ditt nummer är udda")

#%%
A = float(input("Skriv ditt första nummer"))
B = float(input("Skriv ditt andra nummer"))
C = float(input("Skriv ditt tredje nummer"))
D = float(input("Skriv ditt fjärde nummer"))

if A > B and A > C and A > D:
    print(A,"är det största nummret")
elif B > A and A > D and A > C:
    print(B,"är det största nummret")
elif C > A and A > B and A > D:
    print(C,"är det största nummret")
else:
    print(D,"är det största nummret")


#%%
vinkel = float(input("Ange en vinkel i grader"))

if vinkel < 90 and vinkel > 0:
    print("Spetsig vinkel")
elif vinkel == 90:
    print("Rätvinkel")
elif vinkel == 180:
    print("Den e rak")
elif vinkel == 360:
    print("Cirkel bitch")
elif vinkel >= 180:
    print("Den e konvex")
elif vinkel > 90 and vinkel < 180:
    print("Trubbig vinkel")

