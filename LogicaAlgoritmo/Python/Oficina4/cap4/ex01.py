# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:22:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:11:18 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite o nome do usuário e depois disso faça uma
# saudação no formato: "Olá {nome digitado pelo usuário}".

# -*- coding: utf-8 -*-
import os
import time

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Saudação\n")
	time.sleep(2)
	os.system("clear")


def	add_name():
	message = "Insira o seu nome:\t"
	while True:
		try:
			name = str(input(message))
			return (name)
		except ValueError:
			print("Insira um nome válido.")


def	process_greeting(user_name):
	print(f"Olá, {user_name}")


def	main():
	nomePrograma()
	user_name = add_name()
	process_greeting(user_name)
	print("\n\nEncerrando o programa...\n\n")


main()
