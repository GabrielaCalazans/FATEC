# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:25:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/28 16:52:45 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que tenha uma lista com 5 de pessoas, onde cada pessoa tem
# seu nome e sobrenome armazenado em um dicionário, depois disso, exiba todos
# os nomes e sobrenomes. Para complicar um pouco as coisas, vamos simular que
# estes dados foram obtidos da web e com isso recebemos algumas inconsistências.
# Duas das cinco pessoas possuem o dicionário onde as chaves estão em maiúsculo
# e os outros três em minúsculo. 

# pessoas = [  
# {"nome": "Joãozinho", "sobrenome": "da Silva" },  
# {"NOME": "Mariazinha", "SOBRENOME": "de Souza" },  
# {"nome": "Gabriel", "sobrenome": "Schade" },  
# {"NOME": "Joana", "SOBRENOME": "da Silva" },  
# {"nome": "Everton", "sobrenome": "Schmit" },  ]

# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Lista de Pessoas\n")
	time.sleep(2)
	os.system("clear")

people = [  
	{"nome": "Joãozinho", "sobrenome": "da Silva" },
	{"NOME": "Mariazinha", "SOBRENOME": "de Souza" },
	{"nome": "Gabriel", "sobrenome": "Schade" },
	{"NOME": "Joana", "SOBRENOME": "da Silva" },
	{"nome": "Everton", "sobrenome": "Schmit" },]


# Function to normalize dictionary keys
def	normalize_keys(dictonary):
	return ({key.lower(): value for key, value in dictonary.items()})


def	normalize_people(people):
	normalize_people = [normalize_keys(person) for person in people]
	return (normalize_people)


# Display names and surnames
def	display_people(people):
	for person in people:
		name = person.get('nome')
		surname = person.get('sobrenome')
		print(f'{name} {surname}')


# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	print("Lista de Pessoas:")
	print("-" * 30)
	display_people(normalize_people(people))


main()


