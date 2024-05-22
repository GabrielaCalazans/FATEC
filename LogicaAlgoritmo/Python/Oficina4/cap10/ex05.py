# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:49:01 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:56:19 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que solicite dez números ao usuário, depois disso, exiba
# todos os números pares e só então exiba todos os números ímpares.
# Utilize a função Filter para fazer isso.


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Exibição números ímpares - Filter\n")
	time.sleep(2)
	os.system("clear")

