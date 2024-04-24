# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script2.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/24 17:49:10 by gacalaza          #+#    #+#              #
#    Updated: 2024/04/24 17:56:46 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys
import math
math.pi

nota1 = 0
nota2 = 0
media = 0

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = float((nota1 + nota2) / 2)

os.system("clear")
print('\n')

print (f"A média de {nome} é: {media}")
print('\n')

time.sleep(5)
sys.exit
