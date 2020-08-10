vet_let = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
vet_con = []

for item in vet_let:
    if "aeiou".find(item) == -1:
        vet_con.append(item)

print(vet_con)