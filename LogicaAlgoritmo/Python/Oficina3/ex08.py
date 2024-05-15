# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex08.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 20:04:09 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/15 19:57:28 by gacalaza         ###   ########.fr        #
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

class Person:
	def __init__(self, id, club, city, salary):
		self.id = id
		self.time = club
		self.city = city
		self.salary = salary


def	nomePrograma():
	print ("Pesquisa de opnião\n")
	time.sleep(2)
	os.system("clear")

def	show_menu():
	print("Menu:")
	print("1. Para RESPONDER A PESQUISA")
	print("2. Para EXIBIR os resultados até o momento")
	print("5. To EXIT the program")

# • Qual o seu time de coração? 1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 5-Outros
def	ask_club():
	while True:
		try:
			nbr = int(input("Qual o seu time de coração?\n Digite o número correspondente: 1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 5-Outros"))
			if nbr < 1 or nbr > 5:
				raise ValueError('O número deve ser maior que 0 e menor que 6')
			return nbr
		except ValueError:
			print('Digite um número válido')

# • Onde você mora? 1-RJ; 2-Niterói; 3-Outros 
def	ask_city():
	while True:
		try:
			nbr = int(input("Onde você mora?\n Digite o número correspondente: 1-RJ; 2-Niterói; 3-Outros"))
			if nbr < 1 or nbr > 3:
				raise ValueError('O número deve ser maior que 0 e menor que 3')
			return nbr
		except ValueError:
			print('Digite um número válido')

# • Qual o seu salário? 
def	ask_salary():
	while True:
		try:
			nbr = float(input("Qual o seu salário?"))
			return nbr
		except ValueError:
			print('Digite um valor válido')

def	add_answers(i):
	club = ask_club()
	city = ask_city()
	salary = ask_salary()
	person = Person(i, club, city, salary)
	return person

def	result_prog(lst_persons):
	print("oi")

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
			result_prog()
		elif option == "5":
			break
		else:
			print("Opção inválida. Tente novamente.\n")

main()
