# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 15:57:18 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/14 16:28:16 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 5-Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, 
# as caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200 
# volumes, assim, esta transportadora precisa controlar a quantidade e o peso 
# dos volumes para acomodar nos caminhões. Faça um programa que leia n caixas 
# e seu peso, ao final, o programa deve imprimir a quantidade de volumes, o peso 
# total dos volumes e o peso médio dos volumes.

# -*- coding: utf-8 -*-
import os
import time
import sys

def	nomePrograma():
	print ("Calculador de peso\n")
	time.sleep(2)
	os.system("clear")

def	show_menu():
	print("Menu:")
	print("1. Para inserir o peso da caixa a ser colocada no caminhão")
	print("2. Para Exibir a média de peso.")
	print("5. To EXIT the program")

def	add_box(i):
	print(f"Número espaços de caixas disponível {200 - i}")
	while True:
		try:
			box = float(input("Insira o peso da caixa em kg: "))
			return box
		except ValueError:
			print('Digite um número válido')

def	result_prog(boxes, count):
	total = 0
	if (count < 2):
		print("\nNúmero de caixas inseridos insuficinete para realizar a operação")
		print("Tente novamente.\n\n")
		return

	total = sum(boxes)
	media = round(float(total / count), 2)
	print(f"\n\nNúmero de caixas inseridas: {count}\nPeso total das caixas: {total}")
	print(f"A média de peso das caixas inseridas é de: {media}")
	if (total <= 10000):
		print("Peso do caminhão está dentro do esperado.\n\n")
	else:
		print("Peso do caminhão foi excedido, retire algumas caixas e recalcule.\n\n")
		sys.exit()

def	main():
	nomePrograma()
	boxes = []
	i = 0
	while (i < 200):
		show_menu()
		option = input("Escolha uma opção ")

		if option == "1":
			boxes.append(add_box(i))
			i += 1
		elif option == "2":
			result_prog(boxes, i)
		elif option == "5":
			break
		else:
			print("Opção inválida. Tente novamente.\n")
	if (i == 200):
		result_prog(boxes, i)


main()
