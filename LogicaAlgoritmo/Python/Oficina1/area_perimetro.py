# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    area_perimetro.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/24 19:02:50 by gacalaza          #+#    #+#              #
#    Updated: 2024/04/24 20:26:06 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys
import math
math.pi

diametro = 0
perimetro = 0
raio = 0
area = 0
nomePrograma = "Calculo da área de um perímetro de um círculo.\n"

print (nomePrograma)
perimetro = float(input('Digite o perímetro: '))
diametro = perimetro / math.pi
raio = diametro / math.pi
area = (raio**2) * math.pi

os.system("clear")

print('\n')
print (f"O valor da área será de: {area}.")
print('\n')

time.sleep(5)
sys.exit
