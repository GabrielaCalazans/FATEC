# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex08.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 20:04:09 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/14 21:25:31 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 8-Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas: 
# • Qual o seu time de coração? 1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 5-Outros 
# • Onde você mora? 1-RJ; 2-Niterói; 3-Outros 
# • Qual o seu salário? 
# Faça um programa que imprima: 
# • o número de torcedores por clube; 
# • a média salarial dos torcedores do Botafogo; 
# • o número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes; 
# • o número de pessoas de Niterói torcedoras do Fluminense

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

