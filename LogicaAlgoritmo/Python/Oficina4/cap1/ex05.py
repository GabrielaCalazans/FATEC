# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 18:01:47 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/18 18:28:53 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um algoritmo que pergunte ao usuário um número e verifique se ele é primo.
# Também pergunte a idade do usuário e verifique a sua maioridade, depois disso, 
# escreva no console, ‘True’ caso ele já tenha alcançado a maioridade (18 anos), 
# caso contrário escreva ‘False’. 
# Escreva após o cálculo se o número é ou não primo. 
# Pergunte ao usuário se ele quer digitar um novo número e reiniciar o processamento ou finalizar o processamento.


def	is_prime():
	print("É um número primo.")

def	ask_age():
	idade = int(input("Digite a sua idade: "))
	result = True
	if idade >= 18:
		result = True
	else:
		result = False
	print("Maior de idade: %r"% result)