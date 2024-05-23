import csv

def intro():
  print("Welcome to the Spanish and French translator app.\nPlease enter an English word and press the 'Enter' key.\nType 'done' at any time to exit")

def exit():
  print("\nThanks for using the translator app. Have a great day!")

translations = {

}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    #this sets the English header as the dictionary key
    translations[english] = [spanish, french]

done = False

intro()

while not done:
  word = input("\nEnter an English word to translate: ")
  word = word.lower()
  
  if word == "done":
    done = True
    exit()
  #The [word] variable represents the dictionary key. The [0] represents the Spanish word in index 0. You set Spanish words to index 0 when you placed spanish in the first position of the dictionary keys: [spanish,french].
  elif word in translations:
    print((f'\nSPANISH: {translations[word][0]}'))
    print((f'\nFRENCH: {translations[word][1]}'))
  else:
    print("\nTranslation is not known")