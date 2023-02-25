"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zdeněk Pavlásek
email: zpavlasek@gmail.com
"""

# zadani textu
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]
# uzivatele a pomocnici

autorozovani = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"

}
underline = ("-" * 50)
pocet_slov, prvni_velke, cele_velke, cele_male, pouze_cisla, celkem = 0, 0, 0, 0, 0, 0
cisla = []
nejvyzsi_cislo = 0
pocitadlo = 0

# zadej prihlasovací udaje
input_user = input("User: ")
input_pass = input("Pass: ")

# kontrola uzivatele vyreseno slovnikem
if input_user in autorozovani and autorozovani[input_user] == input_pass:
    print(underline)
    print("Vitej uživateli: ", input_user)
    print("Vyber si ze tří textu k analýze")
    print(underline)
    vybrana_volba = int(input("Vyber volbu 1-3:"))
    print(underline)
    if vybrana_volba in (1, 2, 3):
        vybirac = (vybrana_volba - 1)
        pocet_slov = TEXTS[vybirac]
        pocet_slov = pocet_slov.replace(",", "")
        pocet_slov = pocet_slov.replace(".", "")
        pocet_slov = pocet_slov.split()
        print("Počet slov v textu je:", (len(pocet_slov)))
        print(underline)
        for slovo in pocet_slov:
            if slovo[0].isupper():
                prvni_velke += 1
            if slovo.isupper() and slovo.isalpha():
                cele_velke += 1
            if slovo.islower():
                cele_male += 1
            if slovo.isnumeric():
                celkem = int(slovo) + celkem
                pouze_cisla += 1
            graf = len(slovo)
            cisla.append(graf)

        print("Počet slov začínající velkým písmenem je:", prvni_velke)
        print("Počet slov celé s velkých písmen:", cele_velke)
        print("Počet slov celé s malých pismen:", cele_male)
        print("Počet čísel v textu:", pouze_cisla)
        print("Součet čísel je:", celkem)
        print(underline)
        print("LEN     GRAF      POCET")
        print(underline)
        # vyroba grafu toto pro mě bylo hdoně složíté.
        mnozstvi = [0] * (max(cisla))
        for cisla in cisla:
            mnozstvi[cisla - 1] += 1

        for i in mnozstvi:
            pocitadlo += 1

            print("{:2d} | {:<{}s} | {}".format(pocitadlo, "*" * i, 20, i))
else:
    print("špatné jmeno nebo heslo")
