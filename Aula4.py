a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digiou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digiou errado. Segundo bimestre: '))

c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))

d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('media: {}'.format(media))


''''    
a = 0
while a < 10:
    print(a)
    a += 1
'''

'''
#Ex.1 - Números primos
a = int(input('Entre com um valor: ')) #todos os números primos até determinado valor.
for num in range(101):
    div = 0
    for x in range (1, num+1):
        resto = num % x
        if resto == 0:
            div +=  1
    if div == 2:
        print(num)
'''