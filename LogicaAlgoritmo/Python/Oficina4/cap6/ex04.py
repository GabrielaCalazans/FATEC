# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 18:56:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:20:31 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia, solicite ao usuário 10
# números diferentes, um por vez. Caso o número digitado seja par, acrescente
# um ao seu valor. Depois disso, exiba os 10 números digitados. 


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Números\n")
	time.sleep(2)
	os.system("clear")


