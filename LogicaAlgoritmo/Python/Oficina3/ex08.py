# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex08.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 20:04:09 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/21 14:00:26 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 8-Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas: 
# • Qual o seu time de coração? 1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 5-Outros 
# • Onde você mora? 1-RJ; 2-Niterói; 3-Outros 
# • Qual o seu salário? 
# Faça um programa que imprima: 
# • o número de torcedores por clube; 
# • a média salarial dos torcedores do Botafogo; 
# • o número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes; 
# • o número de pessoas de Niterói torcedoras do Fluminense

# -*- coding: utf-8 -*-
import os
import time
import sys

#Classe para representar uma pessoa.
#	Args:
#		id (int): Identificador da pessoa.
#		club (int): Número correspondente ao time de coração da pessoa.
#		city (int): Número correspondente à cidade de residência da pessoa.
#		salary (float): Salário da pessoa.
class Person:
	def __init__(self, id, club, city, salary):
		self.id = id
		self.club = club
		self.city = city
		self.salary = salary

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Pesquisa de opnião\n")
	time.sleep(2)
	os.system("clear")

#	Função menu() exibe um menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1. Para RESPONDER A PESQUISA")
	print("2. Para EXIBIR os resultados até o momento")
	print("5. To EXIT the program")

# Função para perguntar ao usuário sobre o time de coração
# Pergunta ao usuário sobre seu time de coração e retorna a resposta.
#	Returns: int: Número correspondente ao time de coração escolhido pelo usuário.
def	ask_club():
	while True:
		try:
			nbr = int(input("Qual o seu time de coração?\n\tDigite o número correspondente:\n1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 5-Outros "))
			if nbr < 1 or nbr > 5:
				raise ValueError('O número deve ser maior que 0 e menor que 6')
			return nbr
		except ValueError:
			print('Digite um número válido')

# Função para perguntar ao usuário sobre a cidade de residência
# Pergunta ao usuário sobre sua cidade de residência e retorna a resposta.
#	Returns: int: Número correspondente à cidade de residência escolhida pelo usuário.
def	ask_city():
	while True:
		try:
			nbr = int(input("Onde você mora?\n\tDigite o número correspondente:\n 1-RJ; 2-Niterói; 3-Outros "))
			if nbr < 1 or nbr > 3:
				raise ValueError('O número deve ser maior que 0 e menor que 3')
			return nbr
		except ValueError:
			print('Digite um número válido')

# Função para perguntar ao usuário sobre o salário
# Pergunta ao usuário sobre seu salário e retorna a resposta.
#	Returns: float: Salário inserido pelo usuário.
def	ask_salary():
	while True:
		try:
			nbr = float(input("Qual o seu salário? "))
			return nbr
		except ValueError:
			print('Digite um valor válido')

# Função para adicionar as respostas do usuário à pesquisa
# Coleta as respostas do usuário à pesquisa e retorna um objeto Person.
#	Args: i (int): Identificador da pessoa.
#	Returns: Person: Objeto representando a pessoa e suas respostas à pesquisa.
def	add_answers(i):
	club = ask_club()
	city = ask_city()
	salary = ask_salary()
	person = Person(i, club, city, salary)
	return person

# Funções para contar o número de pessoas que escolheram determinada opção
# Conta o número de pessoas que são torcedoras do Fluminense.
#	Args: lst_persons (list): Lista de objetos Person.
#	Returns: int: Número de torcedores do Fluminense.
def	cont_flu(lst_persons):
	target = 1
	i = 0
	for pessoa in lst_persons:
		if pessoa.club == target:
			i += 1
	return i

# Funções para contar o número de pessoas que escolheram determinada opção
# Conta o número de pessoas que são torcedoras do Flamengo.
# Args: lst_persons (list): Lista de objetos Person.
# Returns: int: Número de torcedores do Flamengo.
def	cont_fla(lst_persons):
	target = 4
	i = 0
	for pessoa in lst_persons:
		if pessoa.club == target:
			i += 1
	return i

# Funções para contar o número de pessoas que escolheram determinada opção
# Conta o número de pessoas que são torcedoras do Botafogo.
#	Args: lst_persons (list): Lista de objetos Person.
#	Returns: int: Número de torcedores do Botafogo.
def	cont_bot(lst_persons):
	target = 2
	i = 0
	for pessoa in lst_persons:
		if pessoa.club == target:
			i += 1
	return i

# Funções para contar o número de pessoas que escolheram determinada opção
# Conta o número de pessoas que são torcedoras do Vasco.
#	Args: lst_persons (list): Lista de objetos Person.
#	Returns: int: Número de torcedores do Vasco.
def	cont_vas(lst_persons):
	target = 3
	i = 0
	for pessoa in lst_persons:
		if pessoa.club == target:
			i += 1
	return i

# Funções para contar o número de pessoas que escolheram determinada opção
# Conta o número de pessoas que são torcedoras do Outros clubes.
#	Args: lst_persons (list): Lista de objetos Person.
#	Returns: int: Número de torcedores do Outros clubes.
def	cont_out(lst_persons):
	target = 5
	i = 0
	for pessoa in lst_persons:
		if pessoa.club == target:
			i += 1
	return i

# Função para calcular a soma dos salários dos torcedores do Botafogo
# Calcula a soma dos salários dos torcedores do Botafogo.
#	Args: lst_persons (list): Lista de objetos Person.
#	Returns: float: Soma dos salários dos torcedores do Botafogo.
def	salary_bot(lst_persons):
	target = 2
	i = 0
	for pessoa in lst_persons:
		if pessoa.club == target:
			i += pessoa.salary
	return i

# Funções para contar o número de pessoas que moram no Rio de Janeiro e são torcedoras de outros clubes
# Conta o número de pessoas que moram no Rio de Janeiro e são torcedoras de outros clubes.
# 	Args: lst_persons (list): Lista de objetos Person.
# 	Returns: int: Número de pessoas que moram no Rio de Janeiro e são torcedoras de outros clubes.
def	cont_rj_out(lst_persons):
	target = 1
	i = 0
	for pessoa in lst_persons:
		if pessoa.city == target and pessoa.club == 5:
			i += 1
	return i

# Funções para contar o número de pessoas que moram em Niterói e são torcedoras do Fluminense
# Conta o número de pessoas que moram em Niterói e são torcedoras do Fluminense.
# 	Args: lst_persons (list): Lista de objetos Person.
# 	Returns: int: Número de pessoas que moram em Niterói e são torcedoras do Fluminense.
def	cont_nt_flu(lst_persons):
	target = 2
	i = 0
	for pessoa in lst_persons:
		if pessoa.city == target and pessoa.club == 1:
			i += 1
	return i

# Função para exibir os resultados da pesquisa
# Calcula e exibe os resultados da pesquisa.
# 	Args: lst_persons (list): Lista de objetos Person.
def	result_prog(lst_persons):
	nbr_flu = cont_flu(lst_persons)
	nbr_fla = cont_fla(lst_persons)
	nbr_bot = cont_bot(lst_persons)
	nbr_vas = cont_vas(lst_persons)
	nbr_out = cont_out(lst_persons)
	total_salary_bot = salary_bot(lst_persons)
	media_bot_salary = total_salary_bot / nbr_bot
	nbr_rj_out = cont_rj_out(lst_persons)
	nbr_nt_flu = cont_nt_flu(lst_persons)

	print("\t*** REsultados da pesquisa ***")
	print("Número de torcedores por clube:")
	print(f"\tTotal de Fluminenses: {nbr_flu}")
	print(f"\tTotal de Botafoguenses: {nbr_bot}\n\tTotal de Vascainos: {nbr_vas}")
	print(f"\tTotal de Flamenguistas: {nbr_fla};\n\tTotal de torcedores de outros clubes: {nbr_out}")
	print(f"A média salarial dos torcedores do Botafogo é de: {media_bot_salary}")
	print(f"O número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes: {nbr_rj_out}")
	print(f"O número de pessoas de Niterói torcedoras do Fluminense: {nbr_nt_flu}")

# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	i = 0
	lst_persons = []
	while True:
		show_menu()
		option = input("Escolha uma opção ")
		if option == "1":
			i += 1
			lst_persons.append(add_answers(i))
		elif option == "2":
			result_prog(lst_persons)
		elif option == "5":
			print("Encerrando o programa...")
			break
		else:
			print("Opção inválida. Tente novamente.\n")

main()
