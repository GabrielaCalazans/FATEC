# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 18:56:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/25 15:03:24 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia, solicite ao usuário 10
# números diferentes, um por vez. Caso o número digitado seja par, acrescente
# um ao seu valor. Depois disso, exiba os 10 números digitados. 


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Números\n")
	time.sleep(2)
	os.system("clear")


def	add_nbr(check):
	if (check == 0):
		message = "Insira um número inteiro:\t"
	else:
		message = "Insira mais um número inteiro:\t"
	while True:
		try:
			nbr = int(input(message))
			return (nbr)
		except ValueError:
			print('Digite um número válido\n')


def	append_lst(nbr_lst, nbr):
	nbr_lst.append(nbr)
	return (nbr_lst)


def	display_pair(nbr_lst):
	for x in nbr_lst:
		print(x)


def	main():
	nomePrograma()
	i = 0
	nbr_lst = []
	print("Vamos precisar de 10 números inteiros.")
	while i < 10:
		nbr = add_nbr(i)
		if (nbr % 2 == 0):
			nbr += 1
		nbr_lst = append_lst(nbr_lst, nbr)
		i += 1
	print("Lista de números preenchida:")
	display_pair(nbr_lst)
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()