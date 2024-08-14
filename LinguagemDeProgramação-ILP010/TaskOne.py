# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ExerciseOne.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Gabriela Calazans Andrade Nogueira         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/13 19:41:25 by gacalaza          #+#    #+#              #
#    Updated: 2024/08/13 19:41:25 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math
math.pi
from datetime import date

# **********  Ex. 01 **********
# 1. Crie uma variável para armazenar seu nome e outra para armazenar sua idade.
# Imprima uma mensagem que inclua ambas as informações.

def	ex01():
	print("\n****** Exercise 01 ******\n")
	myName = input("Type your name: ")
	myAge = int(input("Type your age: "))
	dir(myAge)
	print("My name is: " + myName + " and my age is: ", myAge)
	print(f"Variable myName type: {type(myName)} and variable myAge type: {type(myAge)}")
	print(f"\nThe variable 'myName' has all this methods available:\n {dir(myName)}")


# 2. Crie duas variáveis numéricas e realize as quatro operações básicas
# (adição, subtração, multiplicação e divisão). Imprima os resultados.
def	ex02():
	print("\n****** Exercise 02 ******\n")
	n1 = int(input("Type a number: "))
	n2 = int(input("Type another number: "))
	sum = n1 + n2
	subtraction = n1 - n2
	division = n1 / n2
	multiplication = n1 * n2
	print(f"The sum of {n1} + {n2} = {sum}")
	print(f"The subtraticton of {n1} + {n2} = {subtraction}")
	print(f"The division of {n1} + {n2} = {division}")
	print(f"The multiplication of {n1} + {n2} = {multiplication}")


# 3. Crie uma variável do tipo string e outra do tipo float. 
# Concatene as duas variáveis e imprima o resultado. 
def	ex03():
	print("\n****** Exercise 03 ******\n")
	fVar = float(input("Type a number: "))
	strVar = input("Type another number: ")
	print(f"Variable fVar type: {type(fVar)} and variable strVar typ:e {type(strVar)}")
	print(str(fVar) + strVar)


# 4. Crie uma variável booleana e atribua o valor True. 
# Em seguida, inverta o valor utilizando o operador not e imprima o resultado. 
def	ex04():
	print("\n****** Exercise 04 ******\n")
	bVar = True
	print(f"Variable bVar type: {type(bVar)}")
	print(f"Bool variable value: {bVar}")
	print(f"Bool variable value with the 'not' operator: {not bVar}")


# 5. Crie uma variável para armazenar o raio de um círculo.
# Calcule a área do círculo e imprima o resultado. 
def	ex05():
	print("\n****** Exercise 05 ******\n")
	ray = float(input("Type the circle radius: "))
	area = (ray ** 2) * math.pi
	print(f"The area of a circle of radius {ray} is: {area}")


# 6. Crie duas variáveis para armazenar o nome de duas frutas.
# Troque os valores das variáveis e imprima os novos valores. 
def	ex06():
	print("\n****** Exercise 06 ******\n")
	first = input("Type a fruit name: ")
	second = input("Type another fruit  name: ")
	print(f"The variable 'first' holds: {first} and the variable 'second' holds: {second}.")
	temp = first
	first = second
	second = temp
	print(f"After the switch the variable 'first' holds: {first} and the variable 'second' holds: {second}.")


# 7. Crie uma variável para armazenar o seu peso em quilogramas. 
# Converta o peso para libras e imprima o resultado. 
def	ex07():
	print("\n****** Exercise 07 ******\n")
	weightKg = float(input("Type your weight in kilograms: "))
	weightPound = weightKg * 2.205
	print(f"Your weight convert to pounds is equal to: {weightPound}.")


# 8. Crie uma variável para armazenar o seu ano de nascimento.
# Calcule sua idade e imprima o resultado. 
def	ex08():
	print("\n****** Exercise 08 ******\n")
	birthdayYear = int(input("Type the year of your birthday: "))
	currentYear = date.today()
	currentYear = currentYear.strftime('%Y')
	age = int(currentYear) - birthdayYear
	print(f"You have {age} years old.")


# 9. Crie uma variável para armazenar uma frase.
# Conte o número de caracteres na frase e imprima o resultado. 
def	ex09():
	print("\n****** Exercise 09 ******\n")
	phrase = (input("Type a phrase: "))
	print(f"This phrase has {len(phrase)} characteres.")


# 10.	Crie duas variáveis para armazenar dois números inteiros. 
# Verifique se o primeiro número é maior, menor ou igual ao segundo 
# número e imprima o resultado.
def	ex10():
	print("\n****** Exercise 10 ******\n")
	n1 = input("Type a number: ")
	n2 = input("Type another number: ")
	if (n1 > n2):
		print(f"{n1} is bigger than {n2}.")
	else:
		print(f"{n2} is bigger than {n1}.")


def	main():
	ex01()
	ex02()
	ex03()
	ex04()
	ex05()
	ex06()
	ex07()
	ex08()
	ex09()
	ex10()



main()