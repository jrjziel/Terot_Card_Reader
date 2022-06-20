import random

print("Press Y if you would you like to see your tarot reading? ")
input(" ")


tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = random.choice(list(tarot.values()))
spread["present"] = random.choice(list(tarot.values()))
spread["future"] = random.choice(list(tarot.values()))

for key, value in spread.items():
  print("Your " + str(key) + " is the " + value + " card.")
