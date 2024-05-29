# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exA1.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:58:02 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/29 18:11:17 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# A1) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa
# sobre um crime. As perguntas são: 
#     "Telefonou para a vítima?" 
#     "Esteve no local do crime?" 
#     "Mora perto da vítima?" 
#     "Devia para a vítima?" 
#     "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação 
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela 
# deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 
# como "Assassino". Caso contrário, ele será classificado como "Inocente". 


# -*- coding: utf-8 -*-
import os
import time
from collections import Counter

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Detetive\n")
	time.sleep(2)
	os.system("clear")


#	Função menu() exibe um menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1. Para RESPONDER a investigadora")
	print("2. Para EXIBIR os resultados da investigação")
	print("3. To EXIT the program")


def	questions(i):
	if (i == 0):
		return ("Telefonou para a vítima?\t")
	if (i == 1):
		return ("Esteve no local do crime?\t")
	if (i == 2):
		return ("Mora perto da vítima?\t")
	if (i == 3):
		return ("Devia para a vítima?\t" )
	if (i == 4):
		return ("Já trabalhou com a vítima?\t")
	if (i == 5):
		return ("Responda com sim ou não\t")
	if (i == 6):
		return ("Digite o número da sua escolha:\t")


def	add_answer(check):
	while True:
		try:
			answer = str(input(questions(check)))
			if (check != 6 and (answer.lower() != "sim" and answer.lower() != "não")):
				raise ValueError("Resposta inválida. Tente novamente.\n")
			elif (check == 6 and (answer < 1 or answer > 3)):
				raise ValueError("Resposta inválida. Tente novamente.\n")
			return (answer.lower())
		except ValueError:
			print('Resposta inválida. Tente novamente.\n')


def	make_questions():
	person_answers = []
	print(questions(5))
	i = 0
	while i < 5:
		person_answers.append(add_answer(i))
		i += 1
	return (person_answers)


def	conclusion(answers_lst):
	count = Counter(answers_lst)
	nbr_yes = answers_lst.count('sim')
	if nbr_yes == 2:
		return ("Suspeita(o)")
	if nbr_yes > 2 and nbr_yes < 5:
		return ("Cúmplice")
	if nbr_yes == 5:
		return ("Assassina(o)!!!")
	else:
		return ("Inocente")



# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
# Ressalto que match case só funciona em Python3.10 ou mais recente 
def	main():
	nomePrograma()
	answers_lst = []

	answers_lst = make_questions()
	result = conclusion(answers_lst)
	print(f"Você foi classificada(o) como: {result}")
	print("Encerrando o programa...")


main()

