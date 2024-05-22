# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/18 17:40:43 by gacalaza          #+#    #+#              #
#    Updated: 2024/05/22 16:09:53 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Faça um algoritmo que solicite ao usuário que digite o seu nome e a sua idade.
# Multiplique a idade por 12 e some 10. Pule linha e exiba a mensagem 
# “O resultado do Multiplicação da idade por 12 e adicionado 10 é igual a: 
# “e o resultado do cálculo. 

def	add_name():
	return (str(input("Favor inserir o seu nome: ")))


def	add_age():
	return (int(input("Favor inserir a sua idade: ")))


def	main():
	name = add_name()
	age = add_age()
	result = (age * 12) + 10
	print("\n\nO resultado do Multiplicação da idade por 12 e adicionado 10 é igual a: %d"%result, "\n\n")

main()
