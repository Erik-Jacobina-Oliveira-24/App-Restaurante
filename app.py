import os

restaurantes = [{'nome':'Burger King', 'categoria':'Lanche', 'ativo':False},{'nome':'Poke You', 'categoria':'Japonesa', 'ativo':True}, {'nome':'La Fratelli', 'categoria':'Pizzaria', 'ativo':True}]

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_nome_do_programa():
    print('''

    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    ''')

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    #print('3. Remova restaurante')
    print('3. Alterar estado de restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria,'ativo':False }
    
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    
    voltar_ao_menu_principal()
    
def listar_restaurante():
    exibir_subtitulo('Listar restaurantes')

    #print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado' 
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        #Pode ser usado o código abaixo também
        #if ativo == True:
        #    ativo = 'Ativo'
        #else:
        #    ativo = 'Desativado'
        
        #print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

#def remova_restaurantes():
    #exibir_subtitulo('Remova restaurantes')
    
    #remova = input('Digite o restaurante desejado: ')
    #restaurantes.remove(remova)
    #main()

    #voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #o not alterado o estado que está no momento, se caso estiver ativo ele altera para inativo
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso 'if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()

def escolher_opcoes():
    try: #Try encerra o programa se não for uma opção valida, está trelada a def opcao_invalida
        opcao_escolhida = int(input('Escolha uma opção: '))
        #print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        #elif opcao_escolhida == 3:
            #remova_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizando aplicação')

if __name__ == '__main__':
    main()
