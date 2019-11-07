year = eval(input("Enter a year: "))
zodiac = year % 12

ZODIAC = ["monkey", "rooster", "dog", "pig", "rat", "ox",
          "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]

print(ZODIAC[zodiac])
