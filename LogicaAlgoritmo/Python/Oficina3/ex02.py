# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 14:14:19 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/14 15:33:20 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 2- Entrar com o nome e salário de um funcionário. 
# Sabendo-se que o índice de reajuste é de 8 %. 
# Calcular o novo salário. Imprimir Nome, o salário e o novo salário. 
# Pergunte se deseja fazer novos cálculos. 
# Se a resposta for não, encerrar o programa. 
# Se for sim começar novamente pedindo nome e fazendo novos cálculos. 

# -*- coding: utf-8 -*-
import os
import time

def	nomePrograma():
	print ("Calculador de reajuste salarial\n")
	time.sleep(2)
	os.system("clear")

def	add_salary():
	salary = 0
	while True:
		try:
			salary = float(input("Insira o valor do salário: "))
			return salary
		except ValueError:
			print('Digite um número válido')

def	add_name():
	while True:
		try:
			name = str(input("Insira o nome do funcionário: "))
			return name
		except ValueError:
			print('Digite um nome válido')

def	result_prog(salary, name):
	rate = 0.08
	if (salary < 1):
		print("\nValor de salário inseridos insuficinete para realizar a operação.")
		print("Tente novamente.\n\n")
		return

	result = (salary * rate) + salary
	print(f"O salário de {name} com o reajuste passa de {salary} para {result}.\n\n")

def	main():
	nomePrograma()
	option = ""
	while True:
		if option == "não":
			break
		salary = add_salary()
		name = add_name()
		result_prog(salary, name)
		option = input("Deseja fazer novos cálculos? (responda sim ou não)")

main()