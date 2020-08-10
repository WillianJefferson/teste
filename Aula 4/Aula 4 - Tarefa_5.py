vetor_n = []
vetor_p = []
vetor_i = []
item = ""

for i in range(0, 20):
    item = int(input("Digite um número inteiro: "))
    vetor_n.append(item)
    if (item % 2 == 0):
        vetor_p.append(item)
    else:
        vetor_i.append(item)

print(vetor_n)
print(vetor_p)
print(vetor_i)