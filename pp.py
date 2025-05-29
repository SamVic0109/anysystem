import os
current_user = None
users = {}
admin_users = {"Admin": "Admin@1234"}  
login_sucess = False
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def espera():
    input("Pressione qualquer tecla para continuar...")
    
def main_admin():
    while True:
        limpar()
        print(f"Sessão iniciada com: {current_user}")
        save = False

        print('|--------------------------------------|')
        print('|              PAINEL ADM              |')
        print('|--------------------------------------|')
        print('| a) Listar usuários                   |')      
        print('| b) Adicionar Usuário                 |')      
        print('| c) Remover Usuário                   |')
        print('| d) Pesquisar Usuário                 |')
        print('| e) Sair                              |') 
        print('|--------------------------------------|')
        option = (str(input('TECLE A OPÇÃO: '))).strip().lower()

        # filtragem de entrada
        if len(option) != 1 or option not in "abcde":
            print("Opção inválida")
        elif option == "a":
            if users:
                for nome, cpf in users.items():
                    print(f"Nome: {nome} - CPF: {cpf}")
                espera()
            else:
                print("Nenhum usuário cadastrado.") 
                espera()
        elif option == "b":
            limpar()
            while not save:
                    #verifica se o usuário terá conta de administrador
                    is_adm = str(input("O usuário a ser adicionado terá acesso Administrador? (S/N): ")).strip().lower()
                    if is_adm not in "sn":
                        print("Opção inválida")
                    elif is_adm != "s":     
                        nome = str(input("Insira o nome: ")).lower()
                        cpf  = str(input("Insira o CPF: ")).strip().lower()
                        if len(cpf) != 11:
                            print("CPF inválido")
                            limpar()
                        else:
                            confirm = str(input("Confirme se os dados estão corretos: (S/N) ")).strip().lower()
                            print(f"Nome: {nome} \n CPF: {cpf}")
                            if confirm not in "sn":
                                print("opção inválida")
                                limpar()
                            elif confirm != "n":
                                users[nome] = cpf
                                print("USUÁRIO ADICIONADO COM SUCESSO")
                                espera()
                                save = True
                    elif is_adm != "n":
                        while not save:
                            nome = str(input("Digite o nome: "))
                            senha = str(input(str("Digite a senha temporaria: ")))
                            confirm = print(f"Confirme se os dados estão corretos:")
                            print(f"Nome: {nome} \n Senha: {senha}")
                            confirm = str(input("(S)im ou (N)ão: ")).strip().lower()
                            if confirm not in 'sn' or len(confirm) != 1:
                                print("Opção inválida, digite 'S' ou 'N' ")
                            elif confirm == 's':
                                admin_users[nome] = senha
                                print("Usuário adicionado com sucesso!")
                                input("Pressione qualquer tecla para continuar...")
                                save = True
                                    
                            
        elif option == "c":
            limpar()
            print('|--------------------------------------|')
            print('|              EXCLUSÃO                |')
            print('|--------------------------------------|')
            nome = str(input("Digite o nome do usuário: "))
            if nome in users:
                print(f"Usuário encontrado: {users[nome]} ")
                confirm = input("Tem certeza que deseja remover este usuário da lista? (S/N)").strip().lower()
                if confirm == 's':
                    del users[nome]
                    print("Usuário removido com sucesso.")
                    espera()
                else:
                    print("Remoção cancelada.")
                    espera()
            else:
                print("Usuário não encontrado.")
                espera()
        elif option == 'd':
            encontrado = False
            limpar()
            print('|--------------------------------------|')
            print('|              PESQUISA                |')
            print('|--------------------------------------|')
            nome_cpf = str(input("Digite o nome ou CPF: "))
            #consulta
            for nome, cpf in users.items():
                if nome_cpf == nome or nome_cpf == cpf:
                    print(f"Usuário encontrado, Nome: {nome} - CPF: {cpf}")
                    encontrado = True
                    espera()
            if not encontrado:
                print("Usuário não encontrado")
                espera()
        elif option == 'e':
            login()

def main_normal():
    print(f"Sessão iniciada com {current_user}")
    print('|--------------------------------------|')
    print('|              PAINEL                  |')
    print('|--------------------------------------|')

def login():
    limpar()
    global login_sucess
    global current_user
    while not login_sucess:
        print('|--------------------------------------|')
        print('|              LOGIN                   |')
        print('|--------------------------------------|')
        user_name = input("Digite seu nome de usuário: ").strip()
        user_password = input("Digite sua senha: ").strip()
        
        # Verifica se o usuário existe
        if user_name not in admin_users and user_name not in users:
            print("Usuário ou senha incorretos!")
            espera()
            limpar()
            continue  # Volta ao início do loop   
        # Verifica a senha de forma segura
        try:
            if (user_name in admin_users and user_password == admin_users[user_name]):
                print("Login admin efetuado!")
                current_user = user_name
                limpar()
                main_admin()
                login_sucess = True
            elif (user_name in users and user_password == users[user_name]):
                print("Login usuário efetuado!")
                limpar()
                main_normal()
                login_sucess = True
            else:
                print("Usuário ou senha incorretos!")
                espera()
                limpar()
        except KeyError:
            print("Erro no sistema. Usuário não encontrado.")
login()

