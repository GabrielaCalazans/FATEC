# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:40:24 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 20:49:45 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia, depois disso solicite 5
# nomes diferentes ao usuário (utilize laço de repetição). Cada nome digitado
# deve ser adicionado à lista e por fim, todos os nomes devem ser escritos no
# console. Utilize uma função para solicitar e retornar o nome digitado, uma
# função para adicionar o nome à lista (passando o nome e a lista por parâmetro)
# e outra função para escrever todos os nomes no console.


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Criando e Atualizando Lista com Função\n")
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



def	print_lst(name_lst):
	i = 1
	for x in name_lst:
		print(i, x)
		i += 1

def	main():
	nomePrograma()
	i = 0
	name_lst = []
	name_lst = init_name_lst(name_lst)

	print("\n\n")
	print_lst(name_lst)
	print("Encerrando o programa...\n\n")


main()