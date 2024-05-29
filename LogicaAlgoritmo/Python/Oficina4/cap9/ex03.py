# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:40:17 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 17:22:07 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Faça um programa que solicite dois números ao usuário e exiba a multiplicação
# deles. A multiplicação deve ser calculada em uma função.


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Função de Multiplicação\n")
	time.sleep(2)
	os.system("clear")


def	ask_nbr():
	while True:
		try:
			nbr = int(input("Type a number:\t"))
			return nbr
		except ValueError:
			print('Type a valide number')


def	process_mult(n1, n2):
	return (n1 * n2)


def	main():
	nbr1 = ask_nbr()
	nbr2 = ask_nbr()
	result = process_mult(nbr1, nbr2)
	print(f"The result of the multiplication between {nbr1} and {nbr2} is: {result}")

main()
