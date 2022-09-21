lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'logo', 'arara']
lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)




'''
Ex.2
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)
'''

'''
Ex.1
print(lista_animal [1])
nova_lista = lista_animal * 3
print(nova_lista)
# print (sum(lista))
if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('Não existe um lobo na lista')
    lista_animal.append('lobo')
    print(lista_animal)

lista_animal.pop(2)
print(lista_animal)

lista_animal.remove('cachorro')
print(lista_animal)
'''