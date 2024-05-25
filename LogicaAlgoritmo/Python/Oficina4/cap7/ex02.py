# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:21:37 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/25 15:42:04 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista com os valores de 1 até 10 e
# depois exiba apenas os números pares utilizando while. 


# -*- coding: utf-8 -*-
import os
import time

# -*- coding: utf-8 -*-
import os
import time


# Função para exibir o nome do programa
#   Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Números - Exibe Pares\n")
	time.sleep(2)
	os.system("clear")


def	init_lst(nbr_lst):
	i = 1
	while i < 11:
		nbr_lst.append(i)
		i += 1
	return (nbr_lst)


def	display_pair(nbr_lst):
	i = 0
	while i < 10:
		if (nbr_lst[i] % 2 == 0):
			print(nbr_lst[i])
		i += 1


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

