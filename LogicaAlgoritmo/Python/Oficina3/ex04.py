# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/14 15:24:49 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/16 15:39:03 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 4-Dado um número secreto adotado inteiro = 98. 
# O usuário deverá digitar um número até acertar o número secreto. 
# Enquanto a pessoa não acertar, o programa ficara em loop. 
# Se a pessoa não acertou, emita uma mensagem de aviso. 
# Quando a pessoa acertar emita uma mensagem dando parabéns ao usuário.

# -*- coding: utf-8 -*-
import os
import time
import random

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Descubra o número secreto\n")
	time.sleep(2)
	os.system("clear")

# Função para que o usuário tente adivinhar o número secreto
#	Solicita e retorna o número inserido pelo usuário como tentativa de adivinhar o número secreto.
#	Returns: int: Número inserido pelo usuário.
def	guess_nbr():
	while True:
		try:
			nbr = int(input("Tente adivinha qual é o número. Digite um número:"))
			return nbr
		except ValueError:
			print('Digite um número válido')

#	Função para processar a tentativa do usuário e fornecer dicas
#	Compara a tentativa do usuário com o número secreto e fornece dicas.
#	Args:
#		guess (int): Número inserido pelo usuário como tentativa.
#		secret_number (int): Número secreto gerado pelo programa.
#		i (int): Número de tentativas realizadas até o momento.
def	process_guess(guess, secret_number, i ):
	if i == 3:
		print("Ok, parece que está com dificuldades. Vou te ajudar! Agora você vai receber algumas dicas.")
	if guess > secret_number:
		print("Chutou alto, o número secreto é MENOR que isso.\n")
	elif guess + 1 ==  secret_number or guess - 1 ==  secret_number:
		print("Você está muuuuito PERTO do número secreto.\n")
	if guess < secret_number:
		print("Chutou baixo, o número secreto é MAIOR que isso.\n")
	
# Função principal do programa
#	Função principal do programa que gerencia o fluxo de execução.
def	main():
	nomePrograma()
	secret_number = random.randint(1, 500)
	guess = 0
	i = 0

	while True:
		guess = guess_nbr()
		i += 1
		if guess == secret_number:
			print("Parabéns você acertou o número!!")
			print("Encerrando o programa...")
			break
		if i > 0 and i < 3:
			print("continue tentando..")
		if i > 2:
			process_guess(guess, secret_number, i)


main()