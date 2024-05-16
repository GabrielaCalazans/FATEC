# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 14:14:19 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/16 15:31:24 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 2- Entrar com o nome e salário de um funcionário. 
# Sabendo-se que o índice de reajuste é de 8 %. 
# Calcular o novo salário. Imprimir Nome, o salário e o novo salário. 
# Pergunte se deseja fazer novos cálculos. 
# Se a resposta for não, encerrar o programa. 
# Se for sim começar novamente pedindo nome e fazendo novos cálculos. 

# -*- coding: utf-8 -*-
# Importando as bibliotecas necessárias
import os
import time

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Calculador de reajuste salarial\n")
	time.sleep(2)
	os.system("clear")

# Função para adicionar o valor do salário
#	Solicita e retorna o valor do salário inserido pelo usuário.
#	Returns: float: Valor do salário inserido pelo usuário.
def	add_salary():
	salary = 0
	while True:
		try:
			salary = float(input("Insira o valor do salário: "))
			return salary
		except ValueError:
			print('Digite um número válido')

# Função para adicionar o nome do funcionário
#	Solicita e retorna o nome do funcionário inserido pelo usuário.
#	Returns: str: Nome do funcionário inserido pelo usuário.
def	add_name():
	while True:
		try:
			name = str(input("Insira o nome do funcionário: "))
			return name
		except ValueError:
			print('Digite um nome válido')

# Função para calcular e exibir o resultado do programa
#	Calcula e exibe o novo salário do funcionário com o reajuste.
#	Args: 
#		salary (float): Salário do funcionário.
#		name (str): Nome do funcionário.
def	result_prog(salary, name):
	rate = 0.08
	if (salary < 1):
		print("\nValor de salário inseridos insuficinete para realizar a operação.")
		print("Tente novamente.\n\n")
		return

	result = (salary * rate) + salary
	print(f"O salário de {name} com o reajuste passa de {salary} para {result}.\n\n")

# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	option = ""
	while True:
		if option == "não":
			print("Encerrando o programa...")
			break
		salary = add_salary()
		name = add_name()
		result_prog(salary, name)
		option = input("Deseja fazer novos cálculos? (responda sim ou não)")

main()