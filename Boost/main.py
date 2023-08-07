import os
import time

__dirname = os.path.dirname(__file__)
files_counter = 0
username = os.getlogin()

def title(txt):
    print("\n")
    print('=' * (len(txt) + 4))
    print(f'  \033[92m{txt}\033[m')
    print('=' * (len(txt) + 4))

def menu():
    title("Bem vindo ao PC BOOSTER!")
    print("1 - Apagar arquivos temporários")
    print("2 - Mostrar diratório atual")
    print("3 - Mostrar todos os softwares instalados")
    print("4 - Desinstalar software")
    print("5 - Mostrar informações do sistema")
    print("6 - Sair\n")
    user_option = int(input("Digite a opção: "))
    if user_option == 6:
        exit()
    return user_option

user_option = menu()

while user_option != 6:

    files_counter = 0

    if user_option == 1:
        user_option_arquivos = int(input("\n0 - Tudo\n1 - Prefetch\n2 - Temp\n3 - %temp%\n4 - Voltar\nDigite a opção: "))

        # Tudo
        if user_option_arquivos == 0:
            try:
                for file in os.listdir("C:\\Windows\\Prefetch"):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'gsudo del C:\\Windows\\Prefetch\\{file}')
                    files_counter += 1
                for file in os.listdir("C:\\Windows\\Temp"):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'gsudo del C:\\Windows\\Temp\\{file}')
                    files_counter += 1
                for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'gsudo del C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                    files_counter += 1
                print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
                break
            except Exception as error:
                print(f'\033[91mErro: {error}\033[m')

        # Prefetch
        if user_option_arquivos == 1:
            try:
                for file in os.listdir("C:\\Windows\\Prefetch"):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'gsudo del C:\\Windows\\Prefetch\\{file}')
                    files_counter += 1
                print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
                break
            except Exception as error:
                print(f'\033[91mErro: {error}\033[m')

        # TEMP
        if user_option_arquivos == 2:
            try:
                for file in os.listdir("C:\\Windows\\Temp"):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'gsudo del C:\\Windows\\Temp\\{file}')
                    files_counter += 1
                print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
                break
            except Exception as error:
                print(f'\033[91mErro: {error}\033[m')

        # %TEMP%
        if user_option_arquivos == 3:
            try:
                for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'gsudo del C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                    files_counter += 1
                print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
                break
            except Exception as error:
                print(f'\033[91mErro: {error}\033[m')
        
        # Voltar
        if user_option_arquivos == 4:
            menu()

    # Mostrar diretório atual
    if user_option == 2:
        print("\nDiretório atual: ")
        print(f'\n\033[94m{__dirname}\033[m')
        menu()

    # Mostrar todos os softwares instalados
    if user_option == 3:
        print("\n\033[92mSoftwares instalados:\033[m")
        os.system("wmic product get name,version")
        menu()

    # Desinstalar software
    if user_option == 4:
        software_name = input("\nDigite o nome do software: ")
        os.system(f'wmic product where "name like \'%{software_name}%\'" call uninstall')
        print(f'\n\033[92m{software_name} desinstalado com sucesso!\033[m')
        menu()

    # Mostrar informações do sistema
    if user_option == 5:
        print("\n\033[92mInformações do sistema:\033[m")
        os.system("systeminfo")
        menu()

    # Sair
    if user_option == 6:
        print("\033[93mSaindo...\033[m")
        exit()