# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:52:17 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:16:11 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista com o nome das pessoas da sua família.

# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Inicializando uma Lista com Nomes\n")
	time.sleep(2)
	os.system("clear")


def	add_name(i):
	if (i == 0):
		return ("Robson")
	if (i == 1):
		return ("Flor")
	if (i == 2):
		return ("Esmeralda")
	if (i == 3):
		return ("Caroline")
	if (i == 4):
		return ("Gustavo")
	if (i == 5):
		return ("Lilian")


def	init_lst(lst_names):
	i = 0
	while i < 6:
		lst_names.append(add_name(i))
		i += 1
	return (lst_names)


def	main():
	nomePrograma()
	i = 0
	lst_names = []
	lst_names = init_lst(lst_names)

	print("Lista preenchida:")
	for x in lst_names:
		print(x)
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()