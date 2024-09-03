# 1. Escreva um programa no qual leia dois valores numéricos e imprima o maior deles. 
# Caso ambos os números forem iguais, imprima na tela “números iguais”.
def ex01():
    n1 = int(input("Type a number: "))

    n2 = int(input("Type another number: "))

    if (n1 > n2):
        print(f"{n1} is the biggest number.")
    if (n1 < n2):
        print(f"{n2} is the biggest number.")
    else:
        print("The numbers are the same.")


# 2. Escreva um programa que leia um número inteiro e determine se ele é par ou ímpar. 
def ex02():
    n1 = int(input("Type a number: "))
    print(f"The number {n1} is:", end=" ")

    if (n1 % 2 == 0):
        print("pair.")
    else:
        print("odd.")


# 3. Escreva um programa que calcule a média aritmética de 3 números. 
def ex03():
    n1 = int(input("Type a number: "))

    n2 = int(input("Type another number: "))

    n3 = int(input("Type a third number"))

    print("The arithmetic means beatween the tree numbers is: ", ((n1 + n2 + n3) / 3))

# 4. Escreva um programa que leia um número inteiro e imprima a soma dos seus dígitos
def ex04():
    n1 = input("Type a number: ")
    size = len(n1)
    n2 = 0
    if (size == 1):
        print(n1)
    else:
        for i in range(size):
            n2 += int(n1[i])
        print(n2)
            
   
# 5. Escreva um programa que leia 2 números inteiros e informe qual é o maior. 
def ex05():
    n1 = int(input("Type a number: "))

    n2 = int(input("Type another number: "))

    if (n1 > n2):
        print(f"{n1} is bigger than {n2}")
    if (n1 < n2):
        print(f"{n2} is bigger than {n1}")
    else:
        print("The numbers are the same.")


# 6. Ler um número inteiro e exibir o seu sucessor.
def ex06():
    n1 = int(input("Type a number: "))

    print("The next number is: ", n1 + 1)


# 7. Escreva um programa que leia 3 valores e escreva a soma dos 2 maiores
def ex07():
    n1 = int(input("Type a number: "))

    n2 = int(input("Type another number: "))

    n3 = int(input("Type a third number"))

    if n1 > n2:
        if n2 < n3:
            n4 = n1 + n3
        else:
            n4 = n1 + n2
    else:
        if n1 < n3:
            n4 = n2 + n3
        else:
            n4 = n2 + n3

    print("The sum of the two biggest numbers is: ", n4)


# 8. Escreva um programa que imprima todos os números pares do intervalo fechado de 1 a 10.
def ex08():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)

# 9. Escreva um programa que leia 5 números, e imprima a média entre eles.
def ex09():
    for i in range(5):
        if i == 0:
            n = int(input("Type a number: "))
        else:
            n += int(input("Type another number: "))
        

    print("The arithmetic means beatween the five numbers is: ", n / 5)



def main():
    ex01()
    ex02()
    ex03()
    ex04()
    ex05()
    ex06()
    ex07()
    ex08()
    ex09()