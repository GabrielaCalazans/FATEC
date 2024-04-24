# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tempo_queda_livre.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/24 19:02:30 by gacalaza          #+#    #+#              #
#    Updated: 2024/04/24 20:23:17 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# t=√2h/g

# -*- coding: utf-8 -*-
import os
import time 
import sys
import math
math.pi

g = 9.8
altura = 0.0
tq = 0.0
nomePrograma = "Calculo do tempo de queda.\n"

print (nomePrograma)
altura = float(input('Digite a altura: '))
tq = math.sqrt(2 * altura) / g

os.system("clear")

print('\n')
print (f"O tempo de queda será de: {tq}s")
print('\n')

time.sleep(5)
sys.exit


