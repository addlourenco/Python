from aula7_televisao import Televisao
from aula7_calculadora import Calculadora
from Aula8_contador_palavras import contador_letras, teste

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
calculadora = Calculadora(5, 10)
print(calculadora.soma())
lista = ['cachorro', 'gato', 'elefante']
total_letras = contador_letras(lista)
print('total de letras por palavra de lista: {}'.format(total_letras))
print(teste())