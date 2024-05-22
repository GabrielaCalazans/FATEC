# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 15:52:20 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:24:05 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia e solicite ao usuário 3 nomes
# de cidades, um por vez, cada vez que o usuário digitar um nome, o programa
# deve incluir este nome na lista de cidades.

# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Cidades\n")
	time.sleep(2)
	os.system("clear")

def	add_city():
	while True:
		try:
			city = str(input("Insira o nome de uma cidade:\t"))
			return city
		except ValueError:
			print('Digite uma cidade válida')


def	init_lst(cities_lst):
	i = 0
	while i < 3:
		cities_lst.append(add_city())
		i += 1
	return (cities_lst)


def	main():
	nomePrograma()
	i = 0
	cities_lst = []
	cities_lst = init_lst(cities_lst)
	print("Lista preenchida:")
	for x in cities_lst:
		print(x)
	print("\n\n")
	print("Encerrando o programa...\n\n")


main()
