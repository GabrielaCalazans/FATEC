# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/11 20:12:27 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/16 16:38:04 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time
import sys

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Calculador de média de até 20 salários\n")
	time.sleep(2)
	os.system("clear")

#Função menu() exibe um menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1. Para inserir o salário")
	print("2. Para calcular e exibir a média de salários")
	print("5. To EXIT the program")

#Função add_salary(i) para inserir o valor do salário
#recebe o número de posições usadas 'i' e exibe as posições ainda disponíveis para uso
def	add_salary(i):
	print(f"Número de inserções disponíveis {20 - i}")
	while True:
		try:
			salary = float(input("Insira o valor do salário: "))
			return salary
		except ValueError:
			print('Digite um número válido')

# Função result_prog() exibe os resultados no programa
# recebe uma lista com os salários e o contador com o número de salários inseridos até o momento
def	result_prog(salaries, count):
	total = 0
	if (count < 2):
		print("\nNúmero de salário inseridos insuficinete para realizar a operação")
		print("Tente novamente.\n\n")
		return

	total = sum(salaries)
	media = round(float(total / count), 2)
	print(f"A média de salários da empresa é de: {media}\n\n")

#Função principal responsável por chamar cada função no momento correto
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
			print("Encerrando o programa...")
			break
		else:
			print("Opção inválida. Tente novamente.\n")
	if (i == 20):
		result_prog(salaries, i)
		print("Encerrando o programa...")
		sys.exit()


main()
