# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    case_procedure.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/23 14:41:23 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/23 20:50:01 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Para testar os comandos Caso e Procedimentos (Case -Procedure) aprendidos em 
# classe, desenvolva um menu solicitando que o operador selecione qual é o seu
# time predileto e faça uma enquete de qual foi o time mais votado e mostre
# o resultado.

# -*- coding: utf-8 -*-
import os
import time
from collections import Counter

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Tests Case - Procedure\n")
	time.sleep(2)
	os.system("clear")


def	add_club(i):
	if (i == 0):
		return ("1 - São Paulo")
	if (i == 1):
		return ("2 - Corinthians")
	if (i == 2):
		return ("3 - Palmeiras")
	if (i == 3):
		return ("4 - Flamengo")
	if (i == 4):
		return ("5 - Vasco")
	if (i == 5):
		return ("6 - Cruzeiro")
	if (i == 6):
		return ("7 - Grêmio")
	if (i == 7):
		return ("8 - Atlético-MG")
	if (i == 8):
		return ("9 - Bahia")
	if (i == 9):
		return ("10 - Internacional")


def	init_club_lst():
	i = 0
	club_lst = []
	while i < 10:
		club_lst.append(add_club(i))
		i += 1
	return (club_lst)


def	add_nbr(check):
	if (check == 1):
		message = "Digite o número relacionado ao seu time:\t"
	if (check == 2):
		message = "Digite o número de sua escolha:\t"
	while True:
		try:
			nbr = int(input(message))
			if (check == 1 and (nbr < 1 or nbr > 10)):
				raise ValueError("Opção inválida. Tente novamente.\n")
			return (nbr)
		except ValueError:
			print('Digite um número válido\n')


def	add_answers(clubs_lst):
	for x in clubs_lst:
		print(x)
	user_club = add_nbr(1)
	return user_club

#	Função menu() exibe um menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1. Para RESPONDER A PESQUISA de times")
	print("2. Para EXIBIR os resultados da pesquisa")
	print("5. To EXIT the program")


def	count_club(answers_lst, target):
	i = 0
	for x in answers_lst:
		if x == target:
			i += 1
	return i

def	result_research(answers_lst):
	count = Counter(answers_lst)
	most_commom_club = count.most_common(1)[0][0]
	nbr_votes = count.most_common(1)[0][1]
	print("\n\nResultado da pesquisa\n\n")
	print(f"O time mais votado foi: {add_club(most_commom_club - 1)}, ele recebeu {nbr_votes} votos.\n\n")


# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
# Ressalto que match case só funciona em Python3.10 ou mais recente 
def	main():
	nomePrograma()
	answers_lst = []
	clubs_lst = init_club_lst()
	while True:
		show_menu()
		option = add_nbr(2)
		match option:
			case 1:
				answers_lst.append(add_answers(clubs_lst))
			case 2:
				result_research(answers_lst)
			case 5:
				result_research
				print("Encerrando o programa...")
				break
			case _:
				print("Opção inválida. Tente novamente.\n")
	result_research(answers_lst)


main()
