# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 14:49:28 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/14 15:32:55 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 3-Crie um programa que leia o preço de compra e o preço de venda de 10 mercadorias. 
# Para cada mercadoria verificar imprimir se houve lucro e se o lucro foi maior que 15%. 
# Acumule o valor total de mercadorias compradas.

# -*- coding: utf-8 -*-
import os
import time

def	nomePrograma():
	print ("Calculador de Lucro - de compra e venda de mercadoria\n")
	time.sleep(2)
	os.system("clear")

def	add_purchase_goods(i):
	print(f"Número de inserções disponíveis {10 - i}")
	while True:
		try:
			purchase = float(input("Insira o valor de compra da mercadoria: "))
			return purchase
		except ValueError:
			print('Digite um número válido')

def	add_sales_goods(i):
	print(f"Número de inserções disponíveis {10 - i}")
	while True:
		try:
			sales = float(input("Insira o valor de venda da mercadoria: "))
			return sales
		except ValueError:
			print('Digite um número válido')


def	result_prog(sales, purchase):
	profit = 0
	if (sales < 1 or purchase < 1):
		print("\nNúmero de compra ou venda inseridos insuficinete para realizar a operação")
		print("Tente novamente.\n\n")
		return
	profit = sales - purchase
	ideal_profit = (purchase * 0.15)
	if (profit > 0):
		print(f"Houve lucro de {profit}.")
		if (profit >= ideal_profit):
			print(f"Lucro igual ou acima de 15%.\n")
	else:
		print(f"Não há lucro nesta operação. Prejuízo de {profit}\n\n")
	return profit

def	main():
	nomePrograma()
	purchase_total = 0
	sales = 0
	purchase = 0
	profit = 0
	i = 0
	while (i < 10):
		purchase = add_purchase_goods(i)
		purchase_total += purchase
		sales = add_sales_goods(i)
		profit += result_prog(sales, purchase)
		i += 1
	print(f"\n\nValor total de mercadorias copradas {purchase_total}")
	print(f"Lucro Total {profit}\n\n")



main()
