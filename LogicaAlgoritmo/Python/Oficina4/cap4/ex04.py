# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:22:52 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:11:38 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite o nome completo do usuário e exiba somente
# o seu segundo nome/primeiro sobrenome.

# -*- coding: utf-8 -*-
import os
import time

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Exibição de nome formal\n")
	time.sleep(2)
	os.system("clear")


def	add_name():
	message = "Insira o seu nome completo:\t"
	while True:
		try:
			name = str(input(message))
			return (name)
		except ValueError:
			print("Insira um nome válido.")


def	process_name(splited_name):
	print(f"{splited_name[1]}/{splited_name[0]}")


def	main():
	nomePrograma()
	user_name = add_name()
	splited_name = user_name.split()
	process_name(splited_name)
	print("\n\nEncerrando o programa...\n\n")


main()


