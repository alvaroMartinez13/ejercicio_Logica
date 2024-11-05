#Escribir un programa que imprima los 10 primeros números primos comenzando en 2 e imprima también sus respectivos cubos.

def primo():
    for i in range(1, 30):
        print("Número primo: ",i)
        cubo(i)
    

def cubo(num):

     print("Cubo del primo: ",num**3,"\n")

def main(): 
    print()  
    primo()


main()
