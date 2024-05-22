# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:25:27 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:35:10 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista de compras com 5 itens diferentes,
# onde cada item é um dicionário contendo a descrição e preço do produto.
# Depois disso, percorra a lista e exiba as informações de cada item.


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Produtos com Descrição\n")
	time.sleep(2)
	os.system("clear")


