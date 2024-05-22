# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex06.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 14:42:39 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/21 16:35:11 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um algoritmo que solicite um número ao usuário, depois disso, escreva
# ‘True’ no console, caso o número tenha dois dígitos (Esteja entre 10 e 99),
# caso contrário escreva uma mensagem de erro e interrompa o programa.

# -*- coding: utf-8 -*-
import os
import time
import sys

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Verificador de dígitos\n")
	time.sleep(2)
	os.system("clear")

def	add_nbr():
	while True:
		try:
			nbr = int(input("Digite um número: "))
			return (nbr)
		except ValueError:
			print('Digite um número válido')

def	check_digits(n):
	if (n > 9 and n < 100):
		result = True
	else:
		print("ERROR incorrect number")
		result = False
	return (result)

def	main():
	nomePrograma()
	check = True
	while check:
		check = check_digits(add_nbr())

	print("Encerrando o programa...")

main()