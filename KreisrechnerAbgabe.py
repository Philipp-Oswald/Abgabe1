import math

#rad = float(input("Bitte Radius eingeben: "))

#print("der Umfang beträgt: ",2*rad*math.pi)

def eingabe():
    correct = False
    
    while correct == False:        #solange bis korrekte Eingabe
        rad1 = input("eingabe Radius: ")    
        try: 
            rad = float(rad1)
        #Tests, ob Eingabe korrekt
            if rad > 0:
                correct=True
            else:
                print("negativer Radius nicht möglich")
        except ValueError:
            print("keine Zahl")
           
    return rad   
        

radius = eingabe()

kreisumfang = 2*radius*math.pi

print("der Kreisumfang beträgt: ",kreisumfang)