#Wörterbuch Matrix
wb = {"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}

print("Welcome to en2ger, please select the desired function")
print("Choose [T] to translate")
print("Choose [A] to add new word")
    

    
correct = False
    
while correct == False:        #solange bis korrekte Eingabe
    eing = input("Enter a function: ")    
    
    if eing == "T":
        #correct = True #korrekte Eingabe
        word=input("Please enter your word: ") #Auslesen
        if word in wb:
            print("translation: ",wb[word]) #Übersetzung
        else:
            print('not found')
    elif eing == "A":
        #correct = True #korrekte Eingabe
        wb[input('English word:')] = input('German translation:') 
        #warum wird es nicht gespeichert?
        
    else:
        print("Unknown answer")
