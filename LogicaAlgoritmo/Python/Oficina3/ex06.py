# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex06.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 16:28:20 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/14 19:04:30 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 6-Num frigorífico existem 90 bois. 
# Cada boi traz preso em seu pescoço um cartão contendo seu número de identificação e seu peso. 
# Faça um programa que imprima a identificação e o peso do boi mais gordo e do boi 
# mais magro (supondo que não haja empates).

# Dica:
# No exemplo dos bois, o exercício pede que sejam lidos 90 bois, desta forma, 
# é possível utilizar o for, pois sabe-se previamente que são 90, pede também 
# que seja obtido e impresso o boi mais magro e o boi mais gordo, assim, trata-se 
# de um caso de obter o mínimo e o máximo. Além disso, o exercício pede que seja 
# impresso a identificação e o peso, seja ele do mais magro ou do mais gordo.

# No inicio em VAR são as declarações das variáveis, note que, declarou-se a 
# variável idBoi para ler a identificação do boi e pesoBoi para ler o peso do 
# boi, essas duas variáveis é que irão armazenar temporariamente os dados de cada 
# um dos 90 bois. Declarou-se também as variáveis: idBoiGordo e boiGordo para 
# registrar os dados do boi mais gordo e boiMagro para registrar os dados do boi mais
# magro, essas são as variáveis chave da resolução do exercício. 
# 68 Aula 3. 
# Estruturas de Iteração A linha 8 do código proposto inicia o laço for, entre 
# as linhas 9 e 12 é feita a leitura dos dados do boi da iteração atual. 
# O ponto chave para resolver o exercício está entre as linhas 14 e 21, veja 
# que para obter o boi mais gordo foi necessário inicializar a variável na linha 
# 6 e foi realizada a validação do peso do boi lido com o boi registrado, 
# pesoBoi > b A variável boiGordo foi inicializada com zero, assumindo que não 
# exista nenhum boi com peso menor ou igual a zero, então é possível concluir 
# que qualquer peso de boi informado será superior a zero, então na primeira 
# leitura o peso do primeiro boi lido irá substituir o valor da inicialização. 
# Nas iterações seguintes, o peso do novo boi lido só irá substituir o peso e 
# identificação registrados, caso esse novo peso seja maior que o atual, assim, 
# ao fim das iterações o peso do boi mais gordo será registrado na variável 
# boiGordo e a sua respectiva identificação na variável idBoiGordo. 
# O mesmo procedimento é aplicado para o boi magro, foram realizadas apenas duas 
# mudanças, uma é o sinal do operador relacional que passou de maior (>) para menor

# -*- coding: utf-8 -*-
import os
import time
import sys

MAX_BOIS = 90

def	nomePrograma():
	print ("Registrador de peso de gado\n")
	time.sleep(2)
	os.system("clear")

def	show_menu():
	print("Menu:")
	print("1. Para INSERIR o peso e ID do boi")
	print("2. Para EXIBIR os resultados até o momento")
	print("5. To EXIT the program")

def	add_cow_id(i):
	print(f"Total de bois que ainda podem ser inseridos {MAX_BOIS - i}")
	while True:
		try:
			cow_id = int(input("Insira o número do ID do boi: "))
			if cow_id < 0:
				raise ValueError("O ID do boi deve ser um número não negativo.")
			return cow_id
		except ValueError as e:
			print(e)

def	add_cow_weight(i):
	print(f"Total de bois que ainda podem ser inseridos {MAX_BOIS - i}")
	while True:
		try:
			weight = float(input("Insira o PESO do boi: "))
			if weight <= 0:
				raise ValueError("O peso do boi deve ser um número positivo.")
			return weight
		except ValueError as e:
			print(e)

def	result_prog(cattle_id, cattle_weight, count):
	if not cattle_id or not cattle_weight:
		print("\nNenhum boi inserido até o momento.\n")
		return
	lean_cattle = min(cattle_weight)
	lean_id = cattle_id[cattle_weight.index(lean_cattle)]
	
	fat_cattle = max(cattle_weight)
	fat_id = cattle_id[cattle_weight.index(fat_cattle)]
	
	if count < MAX_BOIS:
		print("\nResultados até o momento:")
	print(f"\nO peso do boi mais gordo é: {fat_cattle}\nO ID do boi mais gordo é: {fat_id}\n")
	print(f"\nO peso do boi mais magro é: {lean_cattle}\nO ID do boi mais magro é: {lean_id}\n")

def	main():
	nomePrograma()
	cattle_id = []
	cattle_weight = []
	i = 0
	while (i < MAX_BOIS):
		show_menu()
		option = input("Escolha uma opção ")
		if option == "1":
			cattle_id.append(add_cow_id(i))
			cattle_weight.append(add_cow_weight(i))
			i += 1
		elif option == "2":
			result_prog(cattle_id, cattle_weight, i)
		elif option == "5":
			break
		else:
			print("Opção inválida. Tente novamente.\n")
	if (i == MAX_BOIS):
		result_prog(cattle_id, cattle_weight, i)

main()
