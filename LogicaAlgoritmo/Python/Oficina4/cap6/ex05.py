# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 18:56:35 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/25 15:14:49 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que exiba as tabuadas de 1 até 10 no formato: "2 x 3 = 6",
# (utilize dois comandos for) 


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Tabuadas\n")
	time.sleep(2)
	os.system("clear")


def	process_program():
	i = 0
	for x in range(11):
		print(f"\nTabuada do {i}:")
		for x in range(11):
			if (x == 10):
				print(f"{i} x {x} = ", i * x)
			else:
				print(f"{i} x {x} =  ", i * x)
		i += 1
	print("\n\n")


def	main():
	nomePrograma()
	process_program()
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()