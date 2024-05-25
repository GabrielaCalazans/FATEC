# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 18:56:28 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/25 14:30:41 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que exiba todos os valores ímpares entre 50 e 100 utilizando
# o range. 


# -*- coding: utf-8 -*-
import os
import time

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Listar números ímpares entre um range\n")
	time.sleep(2)
	os.system("clear")


nomePrograma()
for x in range(50, 100):
	if (x % 2 != 0):
		print(x)
