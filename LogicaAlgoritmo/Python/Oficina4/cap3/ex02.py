# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 18:15:56 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:11:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso,
# faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.

# -*- coding: utf-8 -*-
import os
import time
from datetime import date

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Calculadora de maior idade\n")
	time.sleep(2)
	os.system("clear")


def	add_year():
	message = "Digite o ano de seu nascimento:\t"
	while True:
		try:
			user_year = int(input(message))
			if user_year < 0:
				raise ValueError("O ano deve possuir valor positivo.")
			return (user_year)
		except ValueError as e:
			if "could not convert string to float:" in str(e):
				print("Insira uma ano válido.")
			else:
				print(e)


def	process_year(current_year, user_year):
	user_age = int(current_year) - user_year
	if (user_age == 18):
		print("\nVocê completou 18 anos este ano.")
	elif (user_age > 18):
		print(f"\nVocê completou 18 anos há {user_age - 18} anos.")
	else:
		print(f"\nVocê irá completar 18 anos em {18 - user_age} anos.")


def	main():
	nomePrograma()
	current_year = date.today()
	current_year = current_year.strftime('%Y')
	user_year = add_year()
	process_year(current_year, user_year)
	print("\nEncerrando o programa...\n")


main()
