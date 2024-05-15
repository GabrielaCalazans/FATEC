# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex07.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 19:03:46 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/14 20:04:00 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 7-Faça um programa que leia vários números inteiros e apresente o fatorial de cada número. 
# O algoritmo encerra quando se digita um número menor do que 1.

# -*- coding: utf-8 -*-
import os
import time
import sys

NBR_MIN = 1

def	nomePrograma():
	print ("Calculo de fatorial\n")
	time.sleep(2)
	os.system("clear")

def	add_nbr():
	while True:
		try:
			nbr = int(input("Digite um número inteiro: "))
			return nbr
		except ValueError:
			print('Digite um número válido')

def	result_prog(nbr):
	nb = nbr - 1
	result = nbr * nb
	print(f"{nbr}! = {nbr}", end="")
	while nb >= 1:
		print(f" * {nb}", end="")
		nb -= 1
		if nb >= 1:
			result *= nb
	print(" =", result)

def	main():
	nomePrograma()
	nbr = 0
	i = 0
	print("Ao digitar o número '1' o programa será finalizado.")
	while True:
		nbr = add_nbr()
		if nbr == 1:
			break
		result_prog(nbr)

main()
