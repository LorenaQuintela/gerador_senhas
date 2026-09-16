from random import choice, shuffle

lista_letras = ["a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y",
    "z"]
lista_numeros = ["0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"]
lista_simbolos = ["!", "@", "#", "$", "%"]

qtd_letras = int(input("Quantas letras você quer na senha? "))
qtd_numeros = int(input("Quantos números você quer na senha? "))
qtd_simbolos = int(input("Quantos simbolos? "))


lista_aleatória = []

for i in range(qtd_letras):
  letra_aleatoria = choice(lista_letras)
  lista_aleatória.append(letra_aleatoria)