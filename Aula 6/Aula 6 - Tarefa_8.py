string = input('Informe uma string: ').upper()
contrario = string[::-1]

if (string.replace(' ', '') == contrario.replace(' ', '')):
    print('A string é um palindromo')
else:
    print('A string não é um palindromo')