
lista = [1, 10]
try:
    
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
        print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quado não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
