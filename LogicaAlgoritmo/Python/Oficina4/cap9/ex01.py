# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:40:11 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 17:00:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que escreva "Minha primeira função", está escrita deve ser
# realizada a partir da chamada de uma função. 


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	programName():
	print ("Minha primeira função\n")
	time.sleep(2)
	os.system("clear")


def	my_notfirst_func():
	print("This is not my first function.")


def	main():
	my_notfirst_func()

main()