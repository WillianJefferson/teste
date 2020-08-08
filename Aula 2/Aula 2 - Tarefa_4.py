letra = 0


letra = input("Digite uma letra : ")

if ("AEIOU".find(letra.upper()) >= 0):
    print ("VOGAL")
else:
    print ("CONSOANTE")