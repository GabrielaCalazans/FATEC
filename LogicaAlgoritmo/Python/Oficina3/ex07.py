# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex07.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 19:03:46 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/16 16:35:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 7-Faça um programa que leia vários números inteiros e apresente o fatorial de cada número. 
# O algoritmo encerra quando se digita um número menor do que 1.

# -*- coding: utf-8 -*-
import os
import time
import sys

# Definindo o número mínimo para cálculo do fatorial
NBR_MIN = 1

# Função para exibir o nome do programa
# Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Calculo de fatorial\n")
	time.sleep(2)
	os.system("clear")

# Função para adicionar um número inteiro
#	Solicita e retorna um número inteiro inserido pelo usuário.
#	Returns: int: Número inteiro inserido pelo usuário
def	add_nbr():
	while True:
		try:
			nbr = int(input("Digite um número inteiro: "))
			return nbr
		except ValueError:
			print('Digite um número válido')

# Função para calcular e exibir o fatorial do número inserido
#	Calcula e exibe o fatorial do número inserido pelo usuário.
#	Args: nbr (int): Número para o qual o fatorial será calculado.
def	result_prog(nbr):
	nb = nbr - 1
	result = nbr * nb
	print(f"{nbr}! = {nbr}", end="")
	while nb >= 1:
		print(f" * {nb}", end="")
		nb -= 1
		if nb >= NBR_MIN:
			result *= nb
	print(" =", result)

# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	nbr = 0
	i = 0
	print("Ao digitar o número '1' o programa será finalizado.")
	while True:
		nbr = add_nbr()
		if nbr == NBR_MIN:
			print("Encerrando o programa...")
			break
		result_prog(nbr)

main()
