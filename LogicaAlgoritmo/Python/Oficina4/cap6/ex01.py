# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 18:56:20 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:08:24 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista de compras com 5 itens diferentes
# e exiba todos utilizando um laço de repetição. 

# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Compras\n")
	time.sleep(2)
	os.system("clear")


def	add_item(i):
	if (i == 0):
		return ("- pão")
	if (i == 1):
		return ("- detergente")
	if (i == 2):
		return ("- sabão")
	if (i == 3):
		return ("- papel toalha")
	if (i == 4):
		return ("- feijão")


def	init_lst(grocery_lst):
	i = 0
	while i < 5:
		grocery_lst.append(add_item(i))
		i += 1
	return (grocery_lst)


def	main():
	nomePrograma()
	i = 0
	grocery_lst = []
	grocery_lst = init_lst(grocery_lst)

	print("Lista preenchida:")
	for x in grocery_lst:
		print(x)
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()