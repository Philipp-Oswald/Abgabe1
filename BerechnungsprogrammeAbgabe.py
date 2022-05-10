zahl1 = float(input("Bitte Wert1 eingeben: "))
zahl2 = float(input("Bitte Wert2 eingeben: "))

def summe1(Wert1, Wert2):
    summe = zahl1 + zahl2
    return summe

def differenz1(Wert1, Wert2):
    differenz = zahl1 - zahl2
    return differenz

def produkt1(Wert1, Wert2):
    produkt = zahl1 * zahl2
    return produkt

def quotient1(Wert1, Wert2):
    if zahl2 == 0:
        print ("Quotient nicht möglich")
        return
    quotient = zahl1 / zahl2
    return quotient

output1 = summe1(zahl1, zahl2)
output2 = differenz1(zahl1, zahl2)
output3 = produkt1(zahl1, zahl2)
output4 = quotient1(zahl1, zahl2)

print ("Summe: ",output1)
print ("Differenz: ",output2)
print ("Produkt: ",output3)
print ("Quotient: ",output4)
