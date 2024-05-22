# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex07.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/21 14:44:25 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 14:42:33 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Entre com dois números e calcule a potência do número e a raiz quadrada
# e exiba as mensagens dos cálculos. Verifique se o usuário deseja
# continuar o processamento ou encerrar o processamento.

# -*- coding: utf-8 -*-
import os
import time
import math

SQRT = 1
POW_B = 2
POW_E = 3
OPTION = 4

# Função para exibir o nome do programa
#	Exibe o nome do programa e limpa a tela após 2 segundos.
def	nomePrograma():
	print ("Verificador de dígitos\n")
	time.sleep(2)
	os.system("clear")

def	add_nbr(check):
	if (check == SQRT):
		message = "Digite um número para calcular sua raiz:\t"
	if (check == POW_B):
		message = "Digite um número para a base do calculo de potência:\t"
	if (check == POW_E):
		message = "Digite um número para o expoente do calculo de potência:\t"
	if (check == OPTION):
		message = "\n\nDigite 1 para INSERIR novos números ou digite 2 para ENCERRAR o programa:\t"
	while True:
		try:
			nbr = int(input(message))
			if nbr <= 0:
				raise ValueError("O número deve ser positivo.")
			elif check == OPTION and (nbr != 1 and nbr != 2):
				raise ValueError("Opção inválida.")
			return (nbr)
		except ValueError as e:
			if "int() with base 10" in str(e):
				print("O valor deve ser um número inteiro.")
			else:
				print(e)

def	math_process(square, pow_b, pow_e, check):
	if (check == SQRT):
		result = math.sqrt(square)
	if (check == POW_B or check == POW_E):
		result = math.pow(pow_b, pow_e)
	return (result)

def	check_update():
	option = add_nbr(OPTION)
	if (option == 1):
		result = True
	elif (option == 2):
		result = False
	return (result)

def	main():
	nomePrograma()
	check = True
	while check:
		square = add_nbr(SQRT)
		pow_b = add_nbr(POW_B)
		pow_e = add_nbr(POW_E)
		square_r = math_process(square, pow_b, pow_e, 1)
		pow_r = math_process(square, pow_b, pow_e, 2)
		print(f"A raiz quadrada de {square} é igual: {square_r}")
		print(f"{pow_b} elevado a potência {pow_e} é igual: {pow_r}")
		check = check_update()

	print("Encerrando o programa...")

main()