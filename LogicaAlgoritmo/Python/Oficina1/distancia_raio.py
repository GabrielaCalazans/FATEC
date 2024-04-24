# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    distancia_raio.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gacalaza <gacalaza@student.42sp.org.br     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/24 18:03:04 by gacalaza          #+#    #+#              #
#    Updated: 2024/04/24 19:34:40 by gacalaza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-
import os
import time 
import sys
import math
math.pi

distancia = 0
velocidade = 340 #velocidade do som no ar em ms
tempo = 0
nomePrograma = "Calculo da distância de um Raio.\n"

print (nomePrograma)
tempo = float(input('Digite o tempo: '))
distancia = (tempo * velocidade)

os.system("clear")

print('\n')
print (f"A distância do raio será de: {distancia} metros")
print('\n')

time.sleep(5)
sys.exit
