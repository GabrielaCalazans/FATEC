# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:52:25 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 18:52:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia e a preencha com 5 nomes
# diferentes digitados pelo usuário, depois disso solicite um número de 0
# até 4 e remova o elemento desta posição.

# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Nomes\n")
	time.sleep(2)
	os.system("clear")


def	add_name(i):
	if (i == 0):
		message = "Insira um nome:\t"
	else:
		message = "Insira mais um nome:\t"
	while True:
		try:
			name = str(input(message))
			return (name)
		except ValueError:
			print("Insira um nome válido.")


def	add_nbr(check):
	if (check == 1):
		message = "Insira um número inteiro entre 0 e 4:\t"
	if (check == 2):
		message = "Deseja remover mais um item?\n\tDigite 1 para Remover mais um item e 2 para SAIR do programa:\t"
	while True:
		try:
			nbr = int(input(message))
			if (check == 1 and (nbr < 0 or nbr > 4) or check == 2 and (nbr != 1 and nbr != 2)):
				raise ValueError("Opção inválida. Tente novamente.\n")
			return (nbr)
		except ValueError:
			print('Digite um número válido\n')


def	init_name_lst(name_lst):
	i = 0
	while i < 5:
		name_lst.append(add_name(i))
		i += 1
	return (name_lst)


def	remove_name_lst(nbr, name_lst):
	del(name_lst[nbr])
	return (name_lst)

def	print_lst(name_lst):
	for x in name_lst:
		print(x)

def	main():
	nomePrograma()
	i = 0
	name_lst = []
	name_lst = init_name_lst(name_lst)

	print("\n\n")
	while True:
		remove_name_lst(add_nbr(1), name_lst)
		print_lst(name_lst)
		option = add_nbr(2)
		if (option == 1):
			i += 1
		if (option == 2):
			break
		elif (i > 4):
			print("\n\nNão há mais nomes há remover. O programa será encerrado.")
			break
	print("Encerrando o programa...\n\n")


main()