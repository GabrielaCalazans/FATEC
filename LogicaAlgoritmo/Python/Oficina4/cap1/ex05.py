# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 18:01:47 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/21 15:00:32 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um algoritmo que pergunte ao usuário um número e verifique se ele é primo.
# Também pergunte a idade do usuário e verifique a sua maioridade, depois disso, 
# escreva no console, ‘True’ caso ele já tenha alcançado a maioridade (18 anos), 
# caso contrário escreva ‘False’. 
# Escreva após o cálculo se o número é ou não primo. 
# Pergunte ao usuário se ele quer digitar um novo número e reiniciar o processamento ou finalizar o processamento.

# -*- coding: utf-8 -*-
import os
import time
import sys

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Verificador de número primo\n")
	time.sleep(2)
	os.system("clear")

def	is_prime(n):
	i = 2
	if (n == 2):
		result = "é um número primo."
	while (i < n):
		if (n % i == 0 & n != i):
			result = "não é um número primo"
		i += 1
	print(f"O número {n} {result}")

def	ask_age():
	age = int(input("Digite a sua idade: "))
	result = True
	if age >= 18:
		result = True
	else:
		result = False
	print("Maior de idade: %r"% result)
	return (age)

def	main():
	nomePrograma()
	nbr = int(input("Digite um número para verificar se é primo: "))
	is_prime(nbr)
	nbr = ask_age()
	print("Vamos verificar se sua idade é um número primo")
	is_prime(nbr)

main()