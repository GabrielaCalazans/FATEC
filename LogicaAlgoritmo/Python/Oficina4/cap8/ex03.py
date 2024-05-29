# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:25:30 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 19:34:11 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Utilize a lista de compras do programa anterior para identificar qual o
# produto mais barato e qual o produto mais caro da lista de compras.


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Produtos com Descrição\n")
	time.sleep(2)
	os.system("clear")


def	creat_lst():
	descriptions = ["Águas", "Leite", "Carne", "Pizza", "Chocolate"]
	prices = [2.00, 3.00, 18.00, 9.00, 6.50]
	shopping_lst = [dict(Descriptions=desc, Prices=prices)
					for desc, prices in zip(descriptions, prices)]
	return (shopping_lst)

def	print_lst(shopping_lst):
	print("\n\n")
	print("{:<20} {:<10}".format('Description', 'Price ($)'))
	print("-" * 30)
	for item in shopping_lst:
		print("{:<20} {:<10.2f}".format(item['Descriptions'], item['Prices']))
	print("\n\n")


def	process_value(shopping_lst):
	cheaper_item = min(shopping_lst, key=lambda x: x['Prices'])
	expensive_item = max(shopping_lst, key=lambda x: x['Prices'])
	print(f'The cheapest product is {cheaper_item["Descriptions"]} which costs ${cheaper_item["Prices"]:.2f} each')
	print(f'The most expensive product is {expensive_item["Descriptions"]} which costs ${expensive_item["Prices"]:.2f}')
	print("\n\n")


# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	i = 0
	shopping_lst = creat_lst()
	print_lst(shopping_lst)
	process_value(shopping_lst)

main()

