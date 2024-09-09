lista=[]
for x in range(5):
    valor=int(input("Ingresa valor"))
    lista.append(valor)
menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x

print("Lista completa")
print(lista)
print("Menor de lista")
print(menor)
print("Posicion de la menor en la lista")
print(posicion)


