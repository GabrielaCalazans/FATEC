# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script1.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/24 17:48:18 by gacalaza          #+#    #+#              #
#    Updated: 2024/04/24 17:55:16 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys
import math
math.pi

raio = 0
area = 0
nomePrograma = "Calculo da área do círculo.\n"

print (nomePrograma)
raio = float(input('Digite o valor do raio: '))
area = (raio ** 2) * math.pi

os.system("clear")

print('\n')
print (f"A área será de : {area}")
print('\n')

time.sleep(5)
sys.exit
