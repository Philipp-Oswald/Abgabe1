strWetter = input("Geben Sie das Wetter ein[Sonnig oder Regnerisch]: ")
    
if strWetter.upper() == "SONNIG" or strWetter.upper() == "SONNE":
    print("Gartenparty\n")
elif strWetter.upper() == "REGNERISCH" or strWetter.upper() == "REGEN":
    print("Kellerparty\n")
else:
    print("falsche Eingabe\n")
 