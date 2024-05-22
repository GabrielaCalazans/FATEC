# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:25:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:40:05 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que tenha uma lista com 5 de pessoas, onde cada pessoa tem
# seu nome e sobrenome armazenado em um dicionário, depois disso, exiba todos
# os nomes e sobrenomes. Para complicar um pouco as coisas, vamos simular que
# estes dados foram obtidos da web e com isso recebemos algumas inconsistências.
# Duas das cinco pessoas possuem o dicionário onde as chaves estão em maiúsculo
# e os outros três em minúsculo. 


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Pessoas\n")
	time.sleep(2)
	os.system("clear")


