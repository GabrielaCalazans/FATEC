# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:40:24 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:48:25 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que inicialize uma lista vazia, depois disso solicite 5
# nomes diferentes ao usuário (utilize laço de repetição). Cada nome digitado
# deve ser adicionado à lista e por fim, todos os nomes devem ser escritos no
# console. Utilize uma função para solicitar e retornar o nome digitado, uma
# função para adicionar o nome à lista (passando o nome e a lista por parâmetro)
# e outra função para escrever todos os nomes no console.


# -*- coding: utf-8 -*-
import os
import time


 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Criando e Atualizando Lista com Função\n")
	time.sleep(2)
	os.system("clear")


