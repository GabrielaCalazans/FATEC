# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Task04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 16:03:12 by gacalaza          #+#    #+#              #
#    Updated: 2024/09/03 20:38:29 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime


# Escreva um programa para ler o número de lados de um polígono regular e a medida do
# lado (em cm). Calcular e imprimir o seguinte:
# − Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
# − Se o número de lados for igual a 4 e todos os lados forem iguais, escrever QUADRADO e o valor da sua área.
# − Se os números de lados forem iguais a 4 porém 2 lados (bases) são iguais e os outros 2 lados (altura) forem iguais, escrever RETÂNGULO e o valor da sua área.
# − Se o número de lados for inferior a 3, escrever NÃO É UM POLÍGONO
# − Se o número de lados for superior a 4, escrever POLÍGONO NÃO IDENTIFICADO.

def	ex00():
	print("\n\n************EX01 ************\n\n")
	numero_lados = int(input("Digite o número de lados do polígono: "))
	
	if numero_lados < 3:
		print("NÃO É UM POLÍGONO")
		return
	
	if numero_lados == 3:
		lado = float(input("Digite a medida do lado do TRIÂNGULO (em cm): "))
		# Calcula a área do triângulo equilátero
		area = (lado ** 2 * (3 ** 0.5)) / 4
		print(f"TRIÂNGULO com área de {area:.2f} cm²")
	
	elif numero_lados == 4:
		lado1 = float(input("Digite a medida do primeiro lado (em cm): "))
		lado2 = float(input("Digite a medida do segundo lado (em cm): "))
		
		if lado1 == lado2:
			print(f"QUADRADO com área de {lado1 ** 2:.2f} cm²")
		else:
			lado3 = float(input("Digite a medida do terceiro lado (em cm): "))
			lado4 = float(input("Digite a medida do quarto lado (em cm): "))
			if lado1 == lado3 and lado2 == lado4:
				print(f"RETÂNGULO com área de {lado1 * lado2:.2f} cm²")
			else:
				print("POLÍGONO NÃO IDENTIFICADO")
	
	else:
		print("POLÍGONO NÃO IDENTIFICADO")


# ⦁ Faça um algoritmo que retorne ao usuário a sua idade a partir da inserção da sua data
# de nascimento
def	calcular_idade(data_nascimento):
	data_atual = datetime.now()

	idade = data_atual.year - data_nascimento.year
	if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
		idade -= 1
	
	return idade

def	ex01():
	print("\n\n************ EX02 ************\n\n")

	data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
	data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
	
	idade = calcular_idade(data_nascimento)
	print(f"Você tem {idade} anos.")



# ⦁ A empresa Compre+ decidiu dar um aumento de salário aos seus colaboradores e
# necessita de um programa que calcule esses reajustes. Esse programa deve receber o
# salário de um colaborador e fazer o reajuste seguindo os seguintes critérios, baseado no
# salário atual informado:
# salários até R$ 250,00: aumento de 20%
# salários entre R$ 250,00 e R$ 900,00: aumento de 15%
# salários entre R$ 900,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
def calcular_reajuste_salarial(salario_atual):
	# Verifica o percentual de aumento com base no salário atual
	if salario_atual <= 250.00:
		percentual_aumento = 20
	elif 250.00 < salario_atual <= 900.00:
		percentual_aumento = 15
	elif 900.00 < salario_atual <= 1500.00:
		percentual_aumento = 10
	else:
		percentual_aumento = 5
	
	valor_aumento = salario_atual * (percentual_aumento / 100)
	novo_salario = salario_atual + valor_aumento
	
	return percentual_aumento, valor_aumento, novo_salario


def ex02():
	print("\n\n************ EX02 ************\n\n")

	salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

	percentual_aumento, valor_aumento, novo_salario = calcular_reajuste_salarial(salario_atual)
	
	print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
	print(f"Percentual de aumento aplicado: {percentual_aumento}%")
	print(f"Valor do aumento: R$ {valor_aumento:.2f}")
	print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")


# Escreva um algoritmo que peça a sua idade e a idade da sua mãe. Em seguida, imprima
# na tela as 3 informações a seguir:
# a sua idade
# a idade da sua mãe
# minha mãe é <anos> mais velha do que eu
def ex03():
	print("\n\n************ EX03 ************\n\n")

	idade_usuario = int(input("Digite a sua idade: "))
	idade_mae = int(input("Digite a idade da sua mãe: "))
	
	diferenca_idade = idade_mae - idade_usuario
	
	print(f"Sua idade: {idade_usuario} anos")
	print(f"Idade da sua mãe: {idade_mae} anos")
	print(f"Minha mãe é {diferenca_idade} anos mais velha do que eu")



# Desenvolva um programa que simule as 4 operações matemáticas básicas. A entrada
# para a escolha de uma das 4 operações disponíveis é dada da seguinte forma:
# 1. Soma
# 2.Subtração
# 3.Multiplicação
# 4.Divisão
# O usuário deve informar dois números e escolher qual operação deseja fazer de acordo com a lista acima.
def ex04():
	print("\n\n************ EX04 ************\n\n")

	print("Escolha a operação desejada:")
	print("1. Soma")
	print("2. Subtração")
	print("3. Multiplicação")
	print("4. Divisão")
	
	escolha = input("Digite o número correspondente à operação (1/2/3/4): ")

	if escolha not in ['1', '2', '3', '4']:
		print("Escolha inválida. Por favor, escolha uma operação entre 1 e 4.")
		return
	
	numero1 = float(input("Digite o primeiro número: "))
	numero2 = float(input("Digite o segundo número: "))

	if escolha == '1':
		resultado = numero1 + numero2
		print(f"Soma: {numero1} + {numero2} = {resultado}")
	elif escolha == '2':
		resultado = numero1 - numero2
		print(f"Subtração: {numero1} - {numero2} = {resultado}")
	elif escolha == '3':
		resultado = numero1 * numero2
		print(f"Multiplicação: {numero1} * {numero2} = {resultado}")
	elif escolha == '4':
		# Verifica se o segundo número é zero para evitar divisão por zero
		if numero2 == 0:
			print("Erro: Divisão por zero não é permitida.")
		else:
			resultado = numero1 / numero2
			print(f"Divisão: {numero1} / {numero2} = {resultado}")


# Faça um algoritmo investigador criminal. Ele deve fazer 5 perguntas para uma pessoa
# sobre um crime. As perguntas são:
# ⦁ "Telefonou para a vítima?"
# ⦁ "Esteve no local do crime?"
# ⦁ "Mora perto da vítima?"
# ⦁ "Devia para a vítima?"
# ⦁ "Já trabalhou com a vítima?"
# O algoritmo deve emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado
# como "Inocente".
def	ex05():
	print("\n\n************ EX05 ************\n\n")

	perguntas = [
		"Telefonou para a vítima?",
		"Esteve no local do crime?",
		"Mora perto da vítima?",
		"Devia para a vítima?",
		"Já trabalhou com a vítima?"
	]

	respostas_positivas = 0
	
	for pergunta in perguntas:
		resposta = input(pergunta + " (sim/não): ").strip().lower()
		if resposta == "sim":
			respostas_positivas += 1

	if respostas_positivas == 2:
		classificacao = "Suspeita"
	elif 3 <= respostas_positivas <= 4:
		classificacao = "Cúmplice"
	elif respostas_positivas == 5:
		classificacao = "Assassino"
	else:
		classificacao = "Inocente"

	print(f"\nClassificação: {classificacao}")


# Desenvolva um pequeno programa de login e senha. Para isso, peça ao usuário para
# digitar o seu login e armazene em uma variável. Em seguida, peça para o usuário digitar
# a sua senha e armazene em outra variável. Por fim, verifique se o login e a senha são
# iguais àquele definido por você.
# Dicas:
# ⦁ Você pode utilizar para login o seu nome e para a senha o seu CPF
# ⦁ Você deve declarar essas variáveis e armazenar os valores digitados pelo usuário,
# em seguida compare com os valores originais utilizando o SE-SENAO
# ⦁ Caso o login esteja correto, coloque a mensagem “Bem-vindo (nome da pessoa)”,
# caso contrário “Login inválido”
def	ex06():
	print("\n\n************ EX06 ************\n\n")

	login_correto = "Gabriela"  # Use seu nome ou qualquer outro valor para o login
	senha_correta = "123.456.789-00"  # Use seu CPF ou qualquer outro valor para a senha

	login_usuario = input("Digite seu login: ")
	senha_usuario = input("Digite sua senha: ")

	if login_usuario == login_correto and senha_usuario == senha_correta:
		print(f"Bem-vindo(a), {login_usuario}!")
	else:
		print("Login inválido")


# Suponha que você esteja desenvolvendo o sistema de um hotel que deva exibir
# mensagens na recepção para diferentes opções dos hospedes, são elas:
# A) Fazer Check-in
# B) Chamar serviço de quarto
# C )Fazer pedido
# A partir da escolha do usuário, você deve tomar determinadas ações:
# ⦁ Se o usuário escolher A), solicite seu nome, data de entrada e CPF. Depois mostre
# uma mensagem de “Bem-vindo, seu quarto é o número tal”
# ⦁ Se o usuário escolher B), peça para ele informar o número do quarto e informe a
# mensagem “O serviço de quarto está sendo enviado para a acomodação número tal
# (número do quarto fornecido pelo usuário)”
# ⦁ Se o usuário escolher C), pergunte a ele qual seria o pedido e qual quarto ele está,
# depois informe a ele, “O pedido tal (pedido que o usuário fez) está sendo feito,
# aguarde alguns minutos e será entregue no seu quarto (número do quarto)”
def	ex07():
	print("\n\n************ EX08 ************\n\n")

	print("Bem-vindo ao Hotel XYZ. Por favor, escolha uma opção:")
	print("A) Fazer Check-in")
	print("B) Chamar serviço de quarto")
	print("C) Fazer pedido")
	

	escolha = input("Digite a letra correspondente à sua escolha (A/B/C): ").strip().upper()

	if escolha == "A":
		nome = input("Digite seu nome: ")
		data_entrada = input("Digite sua data de entrada (DD/MM/AAAA): ")
		cpf = input("Digite seu CPF: ")
		numero_quarto = 101
		print(f"Bem-vindo(a), {nome}! Seu quarto é o número {numero_quarto}.")
	
	elif escolha == "B":
		numero_quarto = input("Digite o número do seu quarto: ")
		print(f"O serviço de quarto está sendo enviado para a acomodação número {numero_quarto}.")
	
	elif escolha == "C":
		pedido = input("Qual seria o seu pedido? ")
		numero_quarto = input("Digite o número do seu quarto: ")
		print(f"O pedido '{pedido}' está sendo feito. Aguarde alguns minutos e será entregue no seu quarto {numero_quarto}.")
	
	else:
		print("Escolha inválida. Por favor, selecione uma das opções disponíveis (A, B ou C).")



# Leia o código de um determinado produto e mostre sua classificação. Utilize a seguinte
# tabela como referência:
def	ex08():
	print("\n\n************ EX08 ************\n\n")
	codigo = int(input("Digite o código do produto: (número de 1 a 15)"))
	
	if codigo == 1:
		classificacao = "Alimento não-perecível"
	elif codigo in [2, 3, 4]:
		classificacao = "Alimento perecível"
	elif codigo in [5, 6]:
		classificacao = "Vestuário"
	elif codigo == 7:
		classificacao = "Higiene Pessoal"
	elif 8 <= codigo <= 15:
		classificacao = "Limpeza e Utensílios Domésticos"
	else:
		classificacao = "Código inválido"
	
	print(f"A classificação do produto é: {classificacao}")



# Faça um algoritmo que leia um número e exiba o dia correspondente da semana. (1-
# Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
def	ex09():
	print("\n\n************ EX09 ************\n\n")
	numero = int(input("Digite um número de 1 a 7 para saber o dia correspondente da semana: "))
	
	if numero == 1:
		print("1 - Domingo")
	elif numero == 2:
		print("2 - Segunda-feira")
	elif numero == 3:
		print("3 - Terça-feira")
	elif numero == 4:
		print("4 - Quarta-feira")
	elif numero == 5:
		print("5 - Quinta-feira")
	elif numero == 6:
		print("6 - Sexta-feira")
	elif numero == 7:
		print("7 - Sábado")
	else:
		print("Valor inválido")


# Crie um algoritmo que de acordo com a entrada do usuário, ele retorna o gênero de
# acordo com as seguintes informações: Escolha a letra correspondente: F-Feminino, M-
# Masculino, T-Transgênero, N-Não Binário, P-Pangênero, A-Agênero. Pergunte o nome
# do usuário e retorne: “Seu nome é ________ e seu gênero é __________”
def	ex10():
	print("\n\n************ EX10 ************\n\n")
	nome = input("Digite seu nome: ")

	print("Escolha a letra correspondente ao seu gênero:")
	print("F - Feminino")
	print("M - Masculino")
	print("T - Transgênero")
	print("N - Não Binário")
	print("P - Pangênero")
	print("A - Agênero")
	
	genero = input("Digite a letra correspondente ao seu gênero: ").strip().upper()
	
	if genero == "F":
		genero_descricao = "Feminino"
	elif genero == "M":
		genero_descricao = "Masculino"
	elif genero == "T":
		genero_descricao = "Transgênero"
	elif genero == "N":
		genero_descricao = "Não Binário"
	elif genero == "P":
		genero_descricao = "Pangênero"
	elif genero == "A":
		genero_descricao = "Agênero"
	else:
		genero_descricao = "Indefinido"
	
	print(f"Seu nome é {nome} e seu gênero é {genero_descricao}.")



# Faça um algoritmo que ao escolher o numero do país ele retorna qual idioma é falado
# no local de acordo com a tabela abaixo:
# País
# Idioma
# Brasil Português
# China Mandarim
# Argentina Espanhol
# Estados Unidos Inglês
# Portugal Português
# Japão Japonês
def ex11():
	print("\n\n************ EX11 ************\n\n")

	print("Escolha o número do país para saber o idioma falado:")
	print("1 - Brasil")
	print("2 - China")
	print("3 - Argentina")
	print("4 - Estados Unidos")
	print("5 - Portugal")
	print("6 - Japão")
	
	numero = int(input("Digite o número correspondente ao país: "))
	
	if numero == 1:
		idioma = "Português"
	elif numero == 2:
		idioma = "Mandarim"
	elif numero == 3:
		idioma = "Espanhol"
	elif numero == 4:
		idioma = "Inglês"
	elif numero == 5:
		idioma = "Português"
	elif numero == 6:
		idioma = "Japonês"
	else:
		idioma = "Número inválido"
	
	if idioma != "Número inválido":
		print(f"O idioma falado no país selecionado é: {idioma}.")
	else:
		print("Número inválido. Por favor, escolha um número entre 1 e 6.")


def	main():
	ex00()
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
	ex11()


main()