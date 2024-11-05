#Escribir un programa que imprima los 10 primeros números primos comenzando en 2 e imprima también sus respectivos cubos.

numeros = [1,2,3,4,5,6,7,8,9,10]

def primo(lista):
    for i in range(2,len(lista)+1,2):
            print(i)
    

def cubo(lista):
    for i in range(0,len(lista)):
     print("El cubo de ",lista[i]," es: ",lista[i]**3)

def main():
    print("---Primos---")    
    primo(numeros)

    print("\n---Cubos---")
    cubo(numeros)

main()