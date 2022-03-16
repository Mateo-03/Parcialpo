Cifra = int(input("Ingrese el numero que quiere comprobar: "))
lista = []
contador = 0
if Cifra < 0:
  print("Ingrese un numero positivo")
for i in range(1,Cifra+1):
    if (Cifra % i) == 0 :
        contador += 1
        lista.append(i)
print(lista)
if len(lista) > 2:
  print("El numero",Cifra,"si es inteligente")
elif len(lista) <= 2:
    print("El numero",Cifra,"no es inteligente")