# python-kurs.eu/python3_operatoren.php
# Programm, das in 10° Schritten zwischen 0°und 180° den jeweiligen Cosinus-Wert berechnet angibt

import math

Winkel_Grad = 0
while Winkel_Grad <= 180:
    Winkel_Rad = Winkel_Grad *math.pi / 180
    cosinus = math.cos(Winkel_Rad)
    print("Winkel : ", Winkel_Grad, "->cosinus ",cosinus)
    Winkel_Grad += 10