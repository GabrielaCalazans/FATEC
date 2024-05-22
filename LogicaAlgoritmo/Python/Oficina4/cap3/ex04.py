# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 18:17:45 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:09:01 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite ao usuário 2 valores, utilize uma condição
# ternária para escrever qual o maior valor: o primeiro ou o segundo
# (caso os valores sejam iguais, considere o segundo).

# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Classificação Maior Valor\n")
	time.sleep(2)
	os.system("clear")


def	add_nbr(check):
	if (check == 1):
		message = "Insira um número para a verificação:\t"
	if (check == 2):
		message = "Insira outro número para a verificação:\t"
	while True:
		try:
			nbr = float(input(message))
			return (nbr)
		except ValueError as e:
			if "could not convert string to float:" in str(e):
				print("Insira um número válido.")
			else:
				print(e)


def	process_rating(n1, n2):
	return n1 > n2 and n1 or n2


def	main():
	nomePrograma()
	nbr1 = add_nbr(1)
	nbr2 = add_nbr(2)
	max_nbr = process_rating(nbr1, nbr2)
	print("\n\nO maior número é %d\n"%max_nbr)
	print("Encerrando o programa...\n")


main()
