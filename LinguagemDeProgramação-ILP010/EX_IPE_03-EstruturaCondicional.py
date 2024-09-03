# 01 – Escreva um programa no qual leia dois valores numéricos e imprima o maior deles. 
# Caso ambos os números forem iguais, imprima na tela “números iguais”.
def ex01():
	n1 = int(input("Type a number: "))

	n2 = int(input("Type another number: "))

	if (n1 > n2):
		print(f"{n1} is the biggest number.")
	if (n1 < n2):
		print(f"{n2} is the biggest number.")
	else:
		print("The numbers are the same.")


# 02 – Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80 km/h.
def ex02():
	n1 = int(input("Type your car speed in km: "))

	if (n1 > 80):
		print(f"You got a traffic ticket - value: R${(n1 - 80)*5}")
	else:
		print("OK. Safe travel.")



# 03 – Escreva um programa que leia três números e que imprima o maior e o menor.
def ex03():
	n1 = int(input("Type a number: "))

	n2 = int(input("Type another number: "))

	n3 = int(input("Type a third number: "))

	nbrs = [n1, n2, n3]
	biggest = max(nbrs)
	minor = min(nbrs)

	print("The biggest numbers is: ", biggest, "and the minor is: ", minor)


# 04 – Escreve um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
def ex04():
	wage = float(input("Type your wage: "))

	if wage > 1250:
		increase = wage * 0.10
	else:
		increase = wage * 0.15
	print(f"Your salary increase is: R$ {increase:,.2f}. The new total amount will be: R$ {increase+wage:,.2f}")


# 05 – Execute o programa no qual o usuário entre com a idade do carro e caso o valor seja menor ou igual 
# a 3 anos imprima “Seu carro é novo”, caso contrario “Seu carro é velho”.
def ex05():
	age = int(input("Enter the age of your car: "))

	if age <= 3:
		print("\nYour car is new.\n")
	else:
		print("\nYour car is old.\n")

# 06 – Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.
def ex06():
	distance = int(input("Enter your travel distance in km: "))

	if distance <= 200:
		price = distance * 0.5
	else:
		price = distance * 0.45
	print(f"\nYour trip cost will be: R$ {price:,.2f}\n.")


# 07 – Escreva um programa que calcular a categoria de um produto e determine o preço pela tabela: 
# Categoria 1 valor de R$ 10,00; 
# Categoria 2 valor de R$ 15,00; 
# Categoria 3 valor de R$ 19,00; 
# Categoria 4 valor de R$ 23,00 e Categoria 5 valor de R$ 27,00.
def ex07():
	print("\n***Welcome to Cost by Product Category***\n")
	print("We have the following categorys:\n\tCategory 1 - price per unity R$ 10.00\n\tCategory 2 - price per unity R$ 15.00")
	print("\tCategory 3 - price per unity R$ 19.00\n\tCategory 4 - price per unity R$ 23.00\n\tCategory 5 - price per unity R$ 27.00")
	cat = int(input("Type the product category: "))
	qnt = int(input("Type the amount of products: "))

	if cat == 1:
		print(f"The price of your products will be: R$ {qnt * 10}")
	if cat == 2:
		print(f"The price of your products will be: R$ {qnt * 15}")
	if cat == 3:
		print(f"The price of your products will be: R$ {qnt * 19}")
	if cat == 4:
		print(f"The price of your products will be: R$ {qnt * 23}")
	if cat == 5:
		print(f"The price of your products will be: R$ {qnt * 27}")


# 08 – Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada.
def ex08():
	n1 = int(input("Type a number: "))

	n2 = int(input("Type another number: "))

	print("Wich operation you want to do?\n\tType 1 to sum '+' \n\tType 2 to subtration '-' \n\tType 3 to multiplication 'x' or \n\tType 4 to division '/'")
	option = int(input("Type your operation choice"))
	if (option < 1 or option > 4):
		print(f"Invalid option. Please choose a valid option.")
		option = int(input("Type your operation choice: "))
	if (option == 1):
		print(f"The sum of {n1} + {n2} = {n1 + n2}")
	elif (option == 2):
		print(f"The subtration of {n1} - {n2} = {n1 - n2}")
	elif (option == 3):
		print(f"The multiplication of {n1} x {n2} = {n1 * n2}")
	elif (option == 4):
		if n2 == 0:
			print(f"Invalid operation {n1} can not be divide by {n2}")
		else:
			print(f"The division of {n1} / {n2} = {n1 / n2}")


# 09 – Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#  O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação # mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.
def ex09():
	print("***Welcome to your new house mortgage***")
	houseValue = float(input("Enter the value of your choosen house: "))
	years = int(input("Enter how many YEARS will you use to pay the mortgage: "))
	wage = float(input("Enter your wage: "))
	amountPerMonth = houseValue / (years * 12)

	if wage * 0.3 < amountPerMonth:
		print("Invalid mortgage. Your salary is too short for this mortgage.")
		return
	else:
		print(f"Your monthly amount to pay will be: R$ {amountPerMonth:,.2f}")


# 10 – Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencial, I para industrial e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir:
# • Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.
# • Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.
# • Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60.
def ex10():
	print("***Welcome to your energy bill***")
	kWh = float(input("Enter how many kWh you have used: "))

	instalation = input("Type your instalation type:\nR for residential, I for industrial and C for commercial:\t")

	if instalation != 'R' or instalation != 'I' or instalation != 'C':
		print("Invalid option. Please try again. Type only one letter R, I or C\n\n")
		instalation = input("Type your instalation type:\nR for residential, I for industrial and C for commercial:\t")
	if instalation == 'R':
		print("Residential\n")
		if kWh > 500:
			print(f"Your amount to pay is: R$ {kWh * 0.65:,.2f}")
		else:
			print(f"Your amount to pay is: R$ {kWh * 0.4:,.2f}")
	elif instalation == 'I':
		print("Industrial\n")
		if kWh > 5000:
			print(f"Your amount to pay is: R$ {kWh * 0.6:,.2f}")
		else:
			print(f"Your amount to pay is: R$ {kWh * 0.55:,.2f}")
	elif instalation == 'C':
		print("Commercial\n")
		if kWh > 1000:
			print(f"Your amount to pay is: R$ {kWh * 0.6:,.2f}")
		else:
			print(f"Your amount to pay is: R$ {kWh * 0.55:,.2f}")


def main():
	ex01()
	ex02()
	ex03()
	ex04()
	ex05()
	ex06()
	ex07()
	ex08()
	ex09()
	ex10()


main()