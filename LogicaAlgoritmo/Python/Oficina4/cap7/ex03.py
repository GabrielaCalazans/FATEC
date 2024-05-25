# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:21:47 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/25 16:38:42 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia, solicite ao usuário 10
# números ímpares diferentes, um por vez. Caso o número digitado seja par,
# solicite novamente um número, até que o valor seja um número ímpar.
# Depois disso, exiba os 10 números digitados. 


# -*- coding: utf-8 -*-
import os
import time


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Números\n")
	time.sleep(2)
	os.system("clear")


def	add_nbr(check, nbr_lst):
	if (check == 0):
		message = "Insira um número ímpar:\t"
	else:
		message = "Insira mais um número ímpar diferente:\t"
	while True:
		try:
			nbr = int(input(message))
			if (nbr in nbr_lst):
				raise ValueError("O número já foi inserido, insira um número diferente.")
			elif (nbr % 2 == 0):
				raise ValueError("Este número é par. Tente novamente com um número ímpar.")
			return (nbr)
		except ValueError as ve:
			if "int() with base 10" in str(ve):
				print("Insira um número ímpar válido.")
			else:
				print(f'Erro: {ve}\n')
				continue


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
	print("Vamos precisar de 10 números ímpares diferentes.")
	while i < 10:
		nbr = add_nbr(i, nbr_lst)
		nbr_lst = append_lst(nbr_lst, nbr)
		i += 1
	print("Lista de 10 números ímpares preenchida:")
	display_pair(nbr_lst)
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()

