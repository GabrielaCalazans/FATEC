# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fine.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 18:06:39 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/07 18:35:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

def	nomePrograma():
	print ("Calculo de prestaçã em atraso\n")
	time.sleep(1)
	os.system("clear")

def	add_value():
	print("oi")

def	add_days():
	print("oi")

def	show_menu():
	print("Menu:")
	print("1. Para adicionar o VALOR da prestação")
	print("2. Para adicionar os DIAS em atraso")
	print("3. Para EXIBIR os resultados e SAIR do programa")

def	result_prog(value, days):
	print("oi")

def	main():
	nomePrograma()
	value = 0
	days = 0
	while True:
		show_menu()
		option = input("Digite o número de sua escolha: ")

		if option == "1":
			value += add_value()
		elif option == "2":
			days = add_days()
		elif option == "3":
			result_prog(value, days)
			sys.exit()
		else:
			print("Opção inválida. Tente novamente.\n")


main()
