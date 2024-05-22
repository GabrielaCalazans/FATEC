# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:22:34 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:11:24 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite uma mensagem qualquer para o usuário e exiba
# esta mensagem com todas as letras em maiúsculo.

# -*- coding: utf-8 -*-
import os
import time

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Conversor Para Letras Maiúsculas\n")
	time.sleep(2)
	os.system("clear")


def	add_message():
	message = "Insira uma mensagem:\t"
	while True:
		try:
			user_message = str(input(message))
			return (user_message)
		except ValueError:
			print("Insira uma mensagem válida.")


def	process_user_message(user_message):
	print("\n\n", user_message.upper())


def	main():
	nomePrograma()
	user_message = add_message()
	process_user_message(user_message)

	print("\n\nEncerrando o programa...\n\n")


main()