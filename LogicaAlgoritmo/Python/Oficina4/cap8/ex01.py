# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:25:24 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 15:57:38 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que crie um dicionário para definir um produto, contendo sua
# descrição e seu preço.

# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Dicionário de Produtos\n")
	time.sleep(2)
	os.system("clear")


#	Função menu() exibe um menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1. To ADD a product")
	print("2. To DISPLAY all registered products")
	print("5. To EXIT the program")


def	ask_description():
	while True:
		try:
			description = str(input("Type the product description:\t"))
			return description
		except ValueError:
			print('Type a valid description.')

def	ask_price():
	while True:
		try:
			price = float(input("Type the product price:\t"))
			return price
		except ValueError:
			print('Type a valid price.')


def	print_lst(product_lst):
	print("\n\n")
	for item in product_lst:
		print(f"Description: {item['description']}, Price: ${item['price']:.2f}")
	print("\n\n")

# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	i = 0
	product_lst = []
	while True:
		show_menu()
		option = input("Choose an option:\t")
		if option == "1":
			product_lst.append({"description": ask_description(), "price": ask_price()})
		elif option == "2":
			print_lst(product_lst)
		elif option == "5":
			print("\n\nFinishing the program... Bye Bye\n\n")
			break
		else:
			print("Invalid option. Try again.\n")

main()
