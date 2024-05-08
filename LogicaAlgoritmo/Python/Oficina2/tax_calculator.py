# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tax_calculator.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/08 18:13:32 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/08 20:05:52 by gacalaza         ###   ########.fr        #
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
	return float(input("Enter your annual income: "))

def	show_menu():
	print("Menu:")
	print("1. To ENTER your annual income")
	print("2. To DYSPLAY your tax amount")
	print("5. To EXIT the program")

def	result_prog(income):
	tax = 0.0
	if income <= 0:
		print("Invalid income value.\n Please, try again.")
		return
	if income < 85529:
		float(tax = income * 0.18)
		tax_relief = -556
	if income > 85528:
		float(tax = income * 0.32)
		tax_relief = 14839
	if tax <= 0:
		tax = 0.0
		print(f"The tax is: {tax}")
	else:
		print(f"The tax is: {tax} thalers")

def	main():
	nomePrograma()
	income = 0
	while True:
		show_menu()
		option = input("Enter your annual income: ")

		if option == "1":
			income = add_income()
		elif option == "2":
			result_prog(income)
		elif option == "5":
			sys.exit()
		else:
			print("Invalid option. Try again.\n")


main()
