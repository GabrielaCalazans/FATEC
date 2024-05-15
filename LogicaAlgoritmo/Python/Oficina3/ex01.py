# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/11 20:12:27 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/11 22:04:15 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time
import sys

def	nomePrograma():
	print ("Calculador de média de até 20 salários\n")
	time.sleep(2)
	os.system("clear")

def	show_menu():
	print("Menu:")
	print("1. Para inserir o salário")
	print("2. Para calcular e exibir a média de salários")
	print("5. To EXIT the program")

def	add_salary(i):
	print(f"Número de inserções disponíveis {20 - i}")
	while True:
		try:
			salary = float(input("Insira o valor do salário: "))
			return salary
		except ValueError:
			print('Digite um número válido')

def	result_prog(salaries, count):
	total = 0
	if (count < 2):
		print("\nNúmero de salário inseridos insuficinete para realizar a operação")
		print("Tente novamente.\n\n")
		return

	total = sum(salaries)
	media = round(float(total / count), 2)
	print(f"A média de salários da empresa é de: {media}\n\n")

def	main():
	nomePrograma()
	salaries = []
	i = 0
	while (i < 20):
		show_menu()
		option = input("Escolha uma opção ")

		if option == "1":
			salaries.append(add_salary(i))
			i += 1
		elif option == "2":
			result_prog(salaries, i)
		elif option == "5":
			break
		else:
			print("Opção inválida. Tente novamente.\n")
	if (i == 20):
		result_prog(salaries, i)
		sys.exit()


main()
