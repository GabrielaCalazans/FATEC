# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    area_triangulo.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/24 18:03:10 by gacalaza          #+#    #+#              #
#    Updated: 2024/04/24 19:34:48 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys
import math
math.pi

base = 0
altura = 0
area = 0
nomePrograma = "Calculo da área do triangulo.\n"

print (nomePrograma)
base = float(input('Digite a base: '))
altura = float(input('Digite o valor da altura: '))
area = (base * altura) / 2

os.system("clear")

print('\n')
print (f"A área do triângulo será: {area}")
print('\n')

time.sleep(5)
sys.exit
