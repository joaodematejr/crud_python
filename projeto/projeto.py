import datetime
import os.path
import webbrowser

horaAtualComputador = datetime.datetime.now()
''' webbrowser.open('https://pt.stackoverflow.com/admin.php', new=0, autoraise=False) '''

data = horaAtualComputador.strftime("%d/%m/%Y")
hora = horaAtualComputador.strftime("%H:%M")

print('*' * 40)
print('*', ' ' * 36, '*')
print('* Aluno: João Edemar Dematé Junior', ' '*3, '*')
print('* Disciplina: Lógica Computacional', ' '*3, '*')
print(f'* Data Atual: {data}', ' '*13, '*')
print(f'* Hora Atual: {hora}                    *')
print('* Prof: Robertinho', ' '*19, '*')
print('* Python', ' '*29, '*')
print('*', ' ' * 36, '*')
print('*' * 40)

menuEscolha = (input('*' * 3 +
                     ' Menu ' + '*' * 31 + '\n' + '*' * 3 +
                     ' 1 - Cadastrar Telefone' + ' ' * 13 + '*' + '\n' + '*' * 3 +
                     ' 2 - Listar Telefones' + ' ' * 15 + '*' + '\n' + '*' * 3 +
                     ' 3 - Apagar Telefone' + ' ' * 16 + '*' + '\n' + '*' * 3 +
                     ' 0 - Sair' + ' '*27 + '*' + '\n' + '*' * 40 + '\n'))

if menuEscolha == '1':
    print('*' * 3 + ' Cadastro Telefone ' + '*' * 18)
    ''' ENTRADA DO NOME '''
    userNome = str(input('Digite um nome [minimo 4 caracteres]: '))
    while len(userNome) <= 3:
        userNome = str(input('O nome deve ter mais que 3 caracteres: '))
    ''' VERIFICAR SE A PESSOA NÃO DIGITOU NUMERO NO NOME E MENOR QUE 3 '''
    while userNome.isdigit() == True or len(userNome) <= 3:
        userNome = str(input('Idiota !!! aonde já se viu nome com numero :'))
    ''' ENTRADA DO TELEFONE '''
    userTel = list(input('Digite o telefone com 11 digitos : [XXXXXXXXXX]: '))
    ''' VERIFICAR SE O TELEFONE TEM 11 DIGITOS E NÃO DIGITOU LETRAS '''
    while len(userTel) != 11:
        userTel = list(input('Tel Precisa ter 11 digitos: [XXXXXXXXXX]: '))
    for i in range(0, len(userTel)):
        try:
            userTel[i] = int(userTel[i])
            statusDaConversao = True
        except ValueError:
            statusDaConversao = False
            break
    if statusDaConversao == True:
        ''' PEGAR 0 POSIÇÃO E COLOCAR ( '''
        userTel.insert(0, "(")
        ''' PEGAR 3 POSIÇÃO E COLOCAR ) '''
        userTel.insert(3, ")")
        ''' PEGAR 9 POSIÇÃO E COLOCAR - ) '''
        userTel.insert(9, "-")
        ''' CONVERTER TELEFONE PARA STRING '''
        converterTelefoneString = ''.join(map(str, userTel))
        ''' SALVAR AGENDA EM TXT '''
        agendaEmTexto = open('lista_telefônica.txt', 'a')
        documento = userNome + converterTelefoneString + '\n'
        agendaEmTexto.write(documento)
        agendaEmTexto.close()
        print("Documento Salvo Com Sucesso !!!!")
        ''' FAZER BACKUP DA LISTA '''
        arquivoAntigo = open('lista_telefônica.txt', 'r')
        arquivoNovo = open('backup_lista_telefônica.txt', 'w')
        for linhas in arquivoAntigo:
            arquivoNovo.write(linhas)
        arquivoAntigo.close()
        arquivoNovo.close()
        print("Backup realizado com Sucesso")
    else:
        print("Telefone Invalido estamos encerrando o programa !!!")
elif menuEscolha == '2':
    print('*' * 3 + ' Lista Telefones ' + '*' * 20)
    ''' LOCALIZAR AQUIVO, ABRIR LER E EXIBIR NA TELA '''
    verificar = os.path.isfile('lista_telefônica.txt')
    if verificar == False:
        print('Arquivo não localizado !!!')
    else:
        arquivoAgenda = open('lista_telefônica.txt', 'r')
        texto = arquivoAgenda.read()
        print(texto)
        arquivoAgenda.close()
elif menuEscolha == '3':
    print('*' * 3 + ' Apagar Telefone ' + '*' * 20)
    ''' LOCALIZAR AQUIVO, ABRIR LER E EXIBIR NA TELA E DELETAR '''
    verificar = os.path.isfile('lista_telefônica.txt')
    if verificar == False:
        print('Arquivo não localizado !!!')
    else:
        arquivoAgenda = open('lista_telefônica.txt', 'r')
        texto = arquivoAgenda.read()
        print(texto)
        nome = str(input('Digite o nome da Pessoa para Excluir : '))
        if nome == '':
            print('Nome Vazio, você precisa preencher com um nome')
        else:
            confirmacao = int(input('Digite 1 para confirmar a exclusão do ' +
                                    nome + ' da sua agenda ou digite 0 para sair : '))
            if confirmacao == 1:
                ''' NOVA LISTA AONDE SERAO ARMAZENADO A NOVA LISTAGEM DE CONTATOS '''
                novaListaContatos = []
                '''  PERCORRENDO O ARQUIVO E REMOVENDO O CONTATO SELECIONADO  '''
                for linha in open('lista_telefônica.txt', 'r'):
                    if nome not in linha:
                        '''  ADICIONANDO NA NOVA LISTA TODOS OS CONTATOS QUE NÃO FORAM REMOVIDOS  '''
                        novaListaContatos.append(linha)
                '''  LENDO O ARQUIVO  '''
                agendaEmTexto = open('lista_telefônica.txt', 'w')
                '''  CONVERTENDO A LISTA PARA STRING PARA PODER SALVAR  '''
                converterAgendaString = ''.join(map(str, novaListaContatos))
                '''  ESCREVENDO NO ARQUIVO COM NOVA LISTA  '''
                agendaEmTexto.write(converterAgendaString)
                '''  FECHANDO O ARQUIVO   '''
                agendaEmTexto.close()
                print('Usuario ' + nome + ' Removido com Sucesso')
            else:
                print('Operação cancelada')
        arquivoAgenda.close()
elif menuEscolha == '0':
    print('Programa encerrado com Sucesso !!!')
else:
    print('Erro')
