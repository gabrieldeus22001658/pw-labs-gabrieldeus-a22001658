
numero = "1 2 3 21"

print(numero)

lista = numero.split(" ", -1)
sum = 0

for i in range(len(lista)):
    sum += int(lista[i])

print(sum)




