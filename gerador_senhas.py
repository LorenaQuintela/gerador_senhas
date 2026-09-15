from random import random

lista_letras = []
lista_numeros = []
lista_simbolos = []

lista_aleatória = []
qtd_letras = input("Quantas letras você quer na senha? ")
qtd_numeros = input("Quantos números você quer na senha? ")
qtd_simbolos = input("Quantos simbolos? ")
senha_gerada = random(qtd_letras, qtd_numeros, qtd_simbolos)