frase = 'insira a frase aqui a ser analisada'
contagem_espaco = int(frase.count(" "))
contagem_vogais = 0
for i in 'aeiou' :
    contagem_vogais += int(frase.count(i))
print("Espaços:{0}, vogais:{1}".format(contagem_espaco,contagem_vogais))