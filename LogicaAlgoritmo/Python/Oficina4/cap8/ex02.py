# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:25:27 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 16:07:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista de compras com 5 itens diferentes,
# onde cada item é um dicionário contendo a descrição e preço do produto.
# Depois disso, percorra a lista e exiba as informações de cada item.

# lista_compras=[ 
# {"descrição":"Água","preço":2.00}, 
# {"descrição":"Leite","preço":3.00}, 
# {"descrição":"Carne","preço":18.00}, 
# {"descrição":"Pizza","preço":9.00}, 
# {"descrição":"Chocolate","preço":6.50}, ]

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

# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	i = 0
	shopping_lst = creat_lst()
	print_lst(shopping_lst)

main()
