# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:21:47 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:27:45 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia, solicite ao usuário 10
# números ímpares diferentes, um por vez. Caso o número digitado seja par,
# solicite novamente um número, até que o valor seja um número ímpar.
# Depois disso, exiba os 10 números digitados. 


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de números ímpares\n")
	time.sleep(2)
	os.system("clear")


