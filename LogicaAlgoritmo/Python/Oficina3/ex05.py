# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 15:57:18 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/16 15:46:36 by gacalaza         ###   ########.fr        #
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

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Calculador de peso\n")
	time.sleep(2)
	os.system("clear")

# Função para exibir o menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1. Para inserir o peso da caixa a ser colocada no caminhão")
	print("2. Para Exibir a média de peso.")
	print("5. To EXIT the program")

# Função para adicionar o peso de uma caixa
# Solicita e retorna o peso de uma caixa inserido pelo usuário.
#	Args: i (int): Número de caixas já inseridas.
#	Returns: float: Peso da caixa inserido pelo usuário.
def	add_box(i):
	print(f"Número espaços de caixas disponível {200 - i}")
	while True:
		try:
			box = float(input("Insira o peso da caixa em kg: "))
			return box
		except ValueError:
			print('Digite um número válido')

# Função para exibir o resultado do programa
#	Calcula e exibe o número total de caixas inseridas, o peso total das caixas,
#	a média de peso e verifica se o peso total excede o limite do caminhão.
#	Args:
#		boxes (list): Lista contendo os pesos das caixas inseridas.
#		count (int): Número de caixas inseridas.
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
		print("Encerrando o programa...")
		sys.exit()

# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	boxes = []
	box = 0
	total_weight = 0
	i = 0
	while (i < 200):
		show_menu()
		option = input("Escolha uma opção ")

		if option == "1":
			box = add_box(i)
			boxes.append(box)
			total_weight += box
			i += 1
		elif option == "2":
			result_prog(boxes, i)
		elif option == "5":
			print("Encerrando o programa...")
			break
		else:
			print("Opção inválida. Tente novamente.\n")
		if total_weight > 10000:
			print("Peso do caminhão foi excedido, retire algumas caixas e recalcule.\n\n")
			print("Saindo do programa...")
			break
	if (i == 200):
		result_prog(boxes, i)


main()
