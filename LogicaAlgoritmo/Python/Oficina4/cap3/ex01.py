# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 18:15:20 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:10:53 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um algoritmo que solicite 3 notas para o usuário, calcule a média e
# indique se o aluno foi aprovado ou reprovado (nota precisar ser maior ou
# igual à sete para o aluno ser aprovado).

# -*- coding: utf-8 -*-
import os
import time
import sys

GRADE1 = 1
GRADE2 = 2
GRADE3 = 3

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Calculadora de Média de Notas\n")
	time.sleep(2)
	os.system("clear")


def	add_grade(check):
	if (check == GRADE1):
		message = "Digite a primeira nota para calculo da média do aluno:\t"
	if (check == GRADE2):
		message = "Digite a segunda nota:\t"
	if (check == GRADE3):
		message = "Digite a terceira nota:\t"
	while True:
		try:
			grade = float(input(message))
			if grade < 0 or grade > 10:
				raise ValueError("A noda deve ter valor entre 0 e 10.")
			return (grade)
		except ValueError as e:
			if "could not convert string to float:" in str(e):
				print("O valor deve ser um número racional válido.")
			else:
				print(e)


def	process_grade(final_grade):
	if (final_grade < 7):
		result = "Reprovado"
	else:
		result = "Aprovado"
	return (result)


def	main():
	nomePrograma()
	grade1 = add_grade(GRADE1)
	grade2 = add_grade(GRADE2)
	grade3 = add_grade(GRADE3)
	final_grade = (grade1 + grade2 + grade3) / 3
	result = process_grade(final_grade)
	print(f"\n\nMédia do aluno é: %d. \nCom está média o aluno está {result}.\n\n"%final_grade)
	print("Encerrando o programa...\n")


main()