# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:52:23 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 18:21:47 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista com vários números diferentes,
# depois disso, solicite ao usuário um número, verifique se o número está ou
# não na lista e exiba uma mensagem notificando o usuário do resultado.


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Números\n")
	time.sleep(2)
	os.system("clear")


def	add_nbrs(i):
	if (i == 0):
		return (1)
	if (i == 1):
		return (55)
	if (i == 2):
		return (15)
	if (i == 3):
		return (3)
	if (i == 4):
		return (5)
	if (i == 5):
		return (10)


def	add_nbr(check):
	if (check == 1):
		message = "Insira um número inteiro para verificar se está presente na lista:\t"
	if (check == 2):
		message = "Deseja tentar mais uma vez?\n\tDigite 1 para TENTAR NOVAMENTE e 2 para SAIR do programa:\t"
	while True:
		try:
			nbr = int(input(message))
			if (check == 2 and (nbr != 1 and nbr != 2)):
				raise ValueError("Opção inválida. Tente novamente.\n")
			return (nbr)
		except ValueError:
			print('Digite um número válido\n')


def	init_lst(nbrs_lst):
	i = 0
	while i < 6:
		nbrs_lst.append(add_nbrs(i))
		i += 1
	return (nbrs_lst)


def	check_occurrence(nbr, nbrs_lst):
	if (nbr in nbrs_lst):
		return (True)
	else:
		return (False)


def	main():
	nomePrograma()
	i = 0
	nbrs_lst = []
	nbrs_lst = init_lst(nbrs_lst)

	print("\n\n")
	while True:
		nbr = add_nbr(1)
		check = check_occurrence(nbr, nbrs_lst)
		if (check == True):
			print("Parabéns! Acertou um número da lista.")
		if (check == False):
			print(f"Não foi desta vez. O número {nbr} não pertence a lista.")
		option = add_nbr(2)
		if (option == 2):
			break
	print("Encerrando o programa...\n\n")


main()
