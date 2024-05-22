# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/22 19:21:51 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 19:28:54 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um programa que exiba um menu para o usuário selecionar uma das três opções: 
#	1 - Olá mundo 
#	2 - Eu programo em Python 
#	3 - Laços de repetição 
# O programa deve solicitar ao usuário uma das 3 opções, caso o usuário digite
# um valor diferente das opções (1, 2 ou 3), o programa deve apresentar novamente
# o menu de opções até que uma delas seja escolhida. Por fim, o programa deve
# exibir uma mensagem diferente para cada opção.


# -*- coding: utf-8 -*-
import os
import time

 # Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Menu opções\n")
	time.sleep(2)
	os.system("clear")


