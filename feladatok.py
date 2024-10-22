import math
from random import randint

# 4. bekért szám osztói
def negy():
    szam = int(input("Kérlek adj meg egy számot: "))
    print(f"A bekért szám osztói: ")
    for i in range(1, szam + 1):
        if szam % i == 0:
            print(i)


# 6. Faktoriális
def hat():

    szam = int(input("Kérlek adj meg egy számot: "))

    if szam < 0:
        print("A faktoriális csak nem negatív számokra értelmezhető.")
        return

    faktor = 1
    lepesek = ""

    for i in range(1, szam + 1):
        faktor *= i
        lepesek += str(i)
        if i < szam:
            lepesek += " x "

    print(f"{szam}! = {lepesek} = {faktor}")


# 10. Véletlen szám 20-30 között
def tiz():

    print("10 véletlen szám a 20-30-as értéktartományban:")
    for i in range(10):
        veletlen_szam = randint(20, 30)
        print(veletlen_szam)


# 11. Véletlen lottószámok
def tizenegy():

    print("Generált lottószámok: ")
    for i in range(5):
        lotto_szamok = randint(1, 90)
        print(lotto_szamok)
