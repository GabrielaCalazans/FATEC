# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:22:45 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:11:30 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite a idade do usuário, verifique se o texto
# informado só contém números. Caso contenha somente números
# exiba a mensagem: "Você tem {idade digitada} anos.",
# caso contrário exiba a mensagem: "Você digitou uma idade inválida".

# -*- coding: utf-8 -*-
import os
import time

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Verificador de int\n")
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
				print("Você digitou uma idade inválida")
			else:
				print(e)


def	process_print_age(user_age):
	print(f"\n\nVocê tem {user_age} anos.\n\n")


def	main():
	nomePrograma()
	user_age = add_age()
	process_print_age(user_age)

	print("\n\nEncerrando o programa...\n\n")


main()