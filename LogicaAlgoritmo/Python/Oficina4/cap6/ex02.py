# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 18:56:25 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/23 21:47:38 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize que crie uma lista com os valores de 1 até 10
# e depois exiba apenas os números pares. 


# -*- coding: utf-8 -*-
import os
import time


# Função para exibir o nome do programa
#   Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Números - Exibe Pares\n")
	time.sleep(2)
	os.system("cls")


def	init_lst(nbr_lst):
	i = 1
	while i < 11:
		nbr_lst.append(i)
		i += 1
	return (nbr_lst)


def	display_pair(nbr_lst):
	for x in nbr_lst:
		if (x % 2 == 0):
			print(x)


def	main():
	nomePrograma()
	i = 0
	nbr_lst = []
	nbr_lst = init_lst(nbr_lst)
	print("Lista preenchida:")
	display_pair(nbr_lst)
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()
