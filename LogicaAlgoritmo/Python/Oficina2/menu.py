# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    menu.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 17:14:02 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/07 18:08:26 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

def	nomePrograma():
	print ("Menu interativo\n")
	time.sleep(1)
	os.system("clear")

def	show_menu():
	print("Menu:")
	print("1. Para ADICIONAR um número")
	print("2. Para ADICIONAR um nome que irá receber os valores")
	print("3. Para SAIR do programa")

def	add_nbr():
	return int(input("Digite o número que deseja adicionar: "))

def	add_name():
	return input("Digite um nome: ")

def	result_prog(count, nbr, name):
	if count == 0:
		print("Você não adicionou nenhum número.")
	else:
		average = nbr / count
		print(f"Contador de vezes que você inseriu números: {count}")
		print(f"Saldo todal dos valores digitados: {nbr}")
		print(f"Média dos valores digitados: {average}")
	if name == "No name":
		print("O nome da pessoa que recebe os valores não foi definido.")
	else:
		print(f"O nome da pessoa que recebeu os dados é: {name}")

def	main():
	nomePrograma()
	count = 0
	nbr = 0
	name = "No name"
	while True:
		show_menu()
		option = input("Digite o número de sua escolha: ")

		if option == "1":
			count += 1
			nbr += add_nbr()
		elif option == "2":
			count += 1
			name = str(add_name())
		elif option == "3":
			result_prog(count, nbr, name)
			sys.exit()
		else:
			print("Opção inválida. Tente novamente.\n")


main()
