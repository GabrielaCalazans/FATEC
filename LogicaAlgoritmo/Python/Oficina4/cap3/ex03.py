# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 18:16:14 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 14:53:21 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite ao usuário sua idade, depois disso, exiba a
# classificação etária de acordo com as faixas de valores:
#	Criança para 0 até 11 anos;
#	Adolescente para 12 até 18 anos;
#	Jovem para 19 até 24 anos;
#	Adulto para 25 até 40 anos;
#	Meia-Idade para 41 até 60 anos;
#	Idoso acima de 60 anos.

# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Classificação etária\n")
	time.sleep(2)
	os.system("clear")

def	add_age():
	message = "Digite a sua idade:\t"
	while True:
		try:
			age = int(input(message))
			if age < 0:
				raise ValueError("A idade deve possuir valor positivo.")
			return (age)
		except ValueError as e:
			if "invalid literal for int() with base 10:" in str(e):
				print("Insira uma idade válida.")
			else:
				print(e)

def	process_age_rating(user_age):
	if (user_age >= 0 and user_age < 12):
		age_rating = "Criança"
	elif (user_age > 11 and user_age < 19):
		age_rating = "Adolescente"
	elif (user_age > 18 and user_age < 25):
		age_rating = "Jovem"
	elif (user_age > 24 and user_age < 41):
		age_rating = "Adulto"
	elif (user_age > 40 and user_age < 61):
		age_rating = "Meia-Idade"
	else:
		age_rating = "Idoso"
	print(f"\nSua classificação etária é: {age_rating}\n")

def	main():
	nomePrograma()
	user_age = add_age()
	process_age_rating(user_age)
	print("Encerrando o programa...\n")

main()