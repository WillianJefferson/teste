print('Compara duas strings')
string1 = input('String 1: ')
string2 = input('String 2: ')

print('Tamanho de caracteres', (string1, len(string1)))
print('Tamanho de caracteres', (string2, len(string2)))
print('')
if (len(string1) != len(string2)):
    print("As strings são de tamanhos diferentes")
    print("As strings possuem conteúdos diferentes")
else:
    print("As strings tem tamanho igual")
    if (string1 == string2):
        print("As strings possuem o mesmo conteudo")
    else:
        print("As strings possuem o conteudo diferente")