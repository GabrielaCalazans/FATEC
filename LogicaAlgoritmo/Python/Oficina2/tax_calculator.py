# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tax_calculator.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/08 18:13:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/11 19:58:59 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys

def	nomePrograma():
	print ("Tax Calculator\n")
	time.sleep(1)
	os.system("clear")

def	add_income():
	return float(input("Enter the annual income: "))

def	show_menu():
	print("Menu:")
	print("1. To ENTER your annual income")
	print("2. To DYSPLAY your tax amount")
	print("5. To EXIT the program")

def	result_prog(income):
	tax = 0.0
	tax_percent = 0.0
	taxEquality = 0.0
	extra_income = 0
	if income <= 0:
		tax = 0.0
		extra_income = 0.0
	elif income < 85529:
		extra_income = 0.0
		taxEquality = -556.2
		tax_percent = 0.18
	else:
		extra_income = - 85529
		taxEquality = 14839.2
		tax_percent = 0.32
	tax = round(float((income + extra_income) * tax_percent) + taxEquality, 0)
	if tax <= 0:
		tax = 0.0
	print(f"The tax is: {tax} thalers")

def	main():
	nomePrograma()
	income = 0
	while True:
		show_menu()
		option = input("Type your option: ")

		if option == "1":
			income = add_income()
		elif option == "2":
			result_prog(income)
		elif option == "5":
			sys.exit()
		else:
			print("Invalid option. Try again.\n")


main()
