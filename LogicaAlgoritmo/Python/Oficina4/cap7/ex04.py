# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:21:51 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 14:53:45 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que exiba um menu para o usuário selecionar uma das três opções: 
#	1 - Olá mundo 
#	2 - Eu programo em Python 
#	3 - Laços de repetição 
# O programa deve solicitar ao usuário uma das 3 opções, caso o usuário digite
# um valor diferente das opções (1, 2 ou 3), o programa deve apresentar novamente
# o menu de opções até que uma delas seja escolhida. Por fim, o programa deve
# exibir uma mensagem diferente para cada opção.


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Menu opções\n")
	time.sleep(2)
	os.system("clear")


#	Função menu() exibe um menu com 3 opções para o usuário
def	show_menu():
	print("Menu:")
	print("1 - Olá mundo")
	print("2 - Eu programo em Python")
	print("3 - Laços de repetição")


def	add_nbr():
	message = "Digite o número de sua escolha:\t"
	while True:
		try:
			nbr = int(input(message))
			return (nbr)
		except ValueError:
			print('Digite um número válido\n')


def	hello_world():
	print("Hello World!")
	name = str(input("Digite o seu nome:\t"))
	print(f"\nHello {name}!\n\tWelcome to my program =)")
	print("\nFinishing the program. Bye Bye...\n")


def	python_programer():
	name = str(input("Digite o seu nome:\t"))
	print(f"\nHi, {name}\nI'm an IA and I program in Python and I was programed in Python")
	print("Isn't it weird?")
	print("\nFinishing the program. Bye Bye...\n")


def	the_loop_case():
	this = "This "
	message = "message "
	was = "was printed "
	using = "using a "
	repeat = "reapeat loop. =D"
	for x in range(5):
		if (x == 0):
			print(this, end="")
		if (x == 1):
			print(message, end="")
		if (x == 2):
			print(was, end="")
		if (x == 3):
			print(using, end="")
		if (x == 4):
			print(repeat)
	print("\nRepeat loop finished. Bye Bye...\n")

def	main():
	nomePrograma()
	while True:
		show_menu()
		option = add_nbr()
		match option:
			case 1:
				hello_world()
				break
			case 2:
				python_programer()
				break
			case 3:
				the_loop_case()
				break
			case _:
				print("Opção inválida. Tente novamente.\n")


main()