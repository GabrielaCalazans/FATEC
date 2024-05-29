# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:40:14 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 17:08:59 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite o nome do usuário e a idade do usuário,
# depois disso exiba a mensagem: "{nome} possui {idade} anos.".
# Esta mensagem deve ser escrita em uma função. 


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	programName():
	print ("Função com Exibição de Dados\n")
	time.sleep(2)
	os.system("clear")


def	print_data(name, age):
	print(f"{name} is {age} years old.")


def	ask_age():
	while True:
		try:
			age = int(input("Type you age:\t"))
			if age < 1 or age > 120:
				raise ValueError("You're lying")
			return age
		except ValueError:
			print('Type a valide age')


def	main():
	name = str(input("Type you name:\t"))
	age = ask_age()
	print_data(name, age)


main()