# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:40:21 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 20:38:31 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite ao usuário três números diferentes e exiba o
# dobro do maior número. Para fazer isso separe seu código em duas funções
# diferentes: Uma função para retornar o maior dos três números e outra função
# para dobrar o número. 


# -*- coding: utf-8 -*-
import os
import time


# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Função com Calculos de Números\n")
	time.sleep(2)
	os.system("clear")


def	ask_nbr():
	while True:
		try:
			nbr = int(input("Type a number:\t"))
			return nbr
		except ValueError:
			print('Type a valide number')

def	max_nbr(nbr_lst):
	return (max(nbr_lst))


def	double_nbr(nbr):
	return (nbr * 2)


def	main():
	i = 0
	nbr_lst = []
	while i < 3:
		nbr = ask_nbr()
		nbr_lst.append(nbr)
		i += 1
	result = max_nbr(nbr_lst)
	double = double_nbr(result)
	print(f"The largest number is {result} and double this number is {double}.")

main()

