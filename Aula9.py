def escrever_arquivo(texto):
    diretorio = '/media/ade/0393-D61D/FATEC/JOGOS DIGITAIS/2°Semestre/ProgramaçãoII/Python/Projetos/CursoIntroducaoPythonDio/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        texto = arquivo.read()
        print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        notas = lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_media))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'caminho do diretório')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'caminho do diretorio de destino')


if __name__ == '__main__':
    copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira Linha. \n')
    #aluno = 'Rafael,10,10,5,5'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')

