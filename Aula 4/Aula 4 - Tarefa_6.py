def calcMedia(aluno):
    print(f'Notas do aluno {aluno}')
    total=0
    for c in range(0,4):
        total+=float(input(f'Digite a {c+1}ª nota: '))
    return total/4

def mostraMedia(lst):
    aprovado=0
    for v in lst:
        if v>=7:
            aprovado+=1
    print(f'Lista com o resultado das medias: {lst}')
    print(f'Há {aprovado} aluno(s) com media superior a 7,0')

medias=list()

for c in range(0,10):
    medias.append(calcMedia(c+1))
    print()
    mostraMedia(medias)