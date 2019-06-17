import datetime

horaAtualComputador = datetime.datetime.now()

data = horaAtualComputador.strftime("%d/%m/%Y")
hora = horaAtualComputador.strftime("%H:%M")

print('*' * 40)
print('*', ' ' * 36, '*')
print('* Aluno: João Edemar Dematé Junior', ' '*3, '*')
print('* Disciplina: Lógica Computacional', ' '*3, '*')
print(f'* Data Atual: {data}', ' '*13, '*')
print(f'* Hora Atual: {hora}                    *')
print('* Aluno: João Edemar Dematé Junior', ' '*3, '*')
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
        except ValueError:
            print("Telefone Invalido estamos encerrando o programa !!!")
        break
        ''' PEGAR 0 POSIÇÃO E COLOCAR ( '''
        userTel.insert(0, "(")
        ''' PEGAR 3 POSIÇÃO E COLOCAR ) '''
        userTel.insert(3, ")")
        ''' PEGAR 9 POSIÇÃO E COLOCAR - ) '''
        userTel.insert(9, "-")
        ''' CONVERTER TELEFONE PARA STRING '''
        converterTelefoneString = ''.join(map(str, userTel))
        print('Nome : ' + userNome + ' Telefone :', converterTelefoneString)
elif menuEscolha == '2':
    print('Listar Telefones')
elif menuEscolha == '3':
    print('Apagar Telefone')
elif menuEscolha == '0':
    print('Sair')
else:
    print('Erro')


# RASCUNHOS


'''     agenda = []
    agenda.append({'nome': userNome}) '''
