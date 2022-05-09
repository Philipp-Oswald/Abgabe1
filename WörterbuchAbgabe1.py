#Wörterbuch Matrix
mein_woerterbuch = {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon", "marille":"apricot", "pfirsich":"peach"}
# Eingabefeld
word = input("please enter your word here: ")
word = word.lower()
#Ausgabe
print(mein_woerterbuch[word])

#if word.upper() == "word" or word.lower() == "word":
    #print(mein_woerterbuch[word])

#else:
    #print("falsche Eingabe\n")