# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fine.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 18:06:39 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/08 17:17:13 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

def	nomePrograma():
	print ("Calculo de prestação em atraso\n")
	time.sleep(1)
	os.system("clear")

def	add_value():
	return int(input("! Atenção ! SOMENTE números e '.' para separar centavos\nDigite o valor da prestação: "))

def	add_days():
	return int(input("! Atenção ! SOMENTE números\nDigite o números de dias de atraso: "))

def	show_menu():
	print("Menu:")
	print("1. Para adicionar o VALOR da prestação")
	print("2. Para adicionar os DIAS em atraso")
	print("3. Para EXIBIR os resultados")
	print("4. Para SAIR do programa")

def	result_prog(value, days):
	if value | days <= 0:
		print("Informações incompletas para realizar o calculo.\nTente novamente.")
		return
	late_fee = 0.02
	interest_rate_month = 0.01
	interest_rate_day = interest_rate_month / 30
	fine = late_fee * value
	fees = interest_rate_day * days
	pay_amount = value + fees + fine
	if days > 1:
		print(f"Para {days} dias de atraso, temos os seguintes valores:")
	if days == 1:
		print(f"Para {days} dia de atraso, temos os seguintes valores:")
	print(f"Multa {fine} + Juros: {fees} = valor a pagar será de: {pay_amount}")

def	main():
	nomePrograma()
	value = 0
	days = 0
	while True:
		show_menu()
		option = input("Digite o número de sua escolha: ")

		if option == "1":
			value += add_value()
		elif option == "2":
			days = add_days()
		elif option == "3":
			result_prog(value, days)
		elif option == "4":
			sys.exit()
		else:
			print("Opção inválida. Tente novamente.\n")


main()
