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

def main_menu():
    title("Bem vindo ao PC BOOSTER!")
    print("1 - Apagar arquivos temporários")
    print("2 - Mostrar diretório atual")
    print("3 - Mostrar todos os softwares instalados")
    print("4 - Desinstalar software")
    print("5 - Mostrar informações do sistema")
    print("6 - Sair\n")
    user_option = int(input("Digite a opção: "))

def temp_menu():
    user_option_arquivos = int(input("\n0 - Tudo\n1 - Prefetch\n2 - Temp\n3 - %temp%\n4 - Voltar\nDigite a opção: "))

    # Tudo
    if user_option_arquivos == 0:
        try:
            for file in os.listdir("C:\\Windows\\Prefetch"):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do Prefetch
                os.system(f'del /s /q C:\\Windows\\Prefetch\\{file}')
                os.system(f'rmdir /s /q C:\\Windows\\Prefetch\\{file}')
                files_counter += 1

            for file in os.listdir("C:\\Windows\\Temp"):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do Temp
                os.system(f'del /s /q C:\\Windows\\Temp\\{file}')
                os.system(f'rmdir /s /q C:\\Windows\\Temp\\{file}')
                files_counter += 1

            for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do %temp%
                os.system(f'del /s /q C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                os.system(f'rmdir /s /q C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                files_counter += 1

            print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

    # Prefetch
    if user_option_arquivos == 1:
        try:
            for file in os.listdir("C:\\Windows\\Prefetch"):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do Prefetch
                os.system(f'del /s /q C:\\Windows\\Prefetch\\{file}')
                os.system(f'rmdir /s /q C:\\Windows\\Prefetch\\{file}')
                files_counter += 1
            print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

    # TEMP
    if user_option_arquivos == 2:
        try:
            for file in os.listdir("C:\\Windows\\Temp"):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do Temp
                os.system(f'del /s /q C:\\Windows\\Temp\\{file}')
                os.system(f'rmdir /s /q C:\\Windows\\Temp\\{file}')
                files_counter += 1
            print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

    # %TEMP%
    if user_option_arquivos == 3:
        try:
            for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do %temp%
                os.system(f'del /s /q C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                os.system(f'rmdir /s /q C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                files_counter += 1
            print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')
    
    # Voltar
    if user_option_arquivos == 4:
        print()

def main():
    files_counter = 0
    
    while True:
        main_menu():


    try:
        # Apagar arquivos temporários
        if user_option == 1:
            

        # Mostrar diretório atual
        if user_option == 2:
            print("\nDiretório atual: ")
            print(f'\n\033[94m{__dirname}\033[m')

        # Mostrar todos os softwares instalados
        if user_option == 3:
            print("\n\033[92mSoftwares instalados:\033[m")
            os.system("wmic product get name,version")

        # Desinstalar software
        if user_option == 4:
            software_name = input("\nDigite o nome do software: ")
            os.system(f'wmic product where "name like \'%{software_name}%\'" call uninstall')
            print(f'\n\033[92m{software_name} desinstalado com sucesso!\033[m')

        # Mostrar informações do sistema
        if user_option == 5:
            print("\n\033[92mInformações do sistema:\033[m")
            os.system("systeminfo")

        # Sair
        if user_option == 6:
            print("\033[93mSaindo...\033[m")
            exit()

    except ValueError:
        print(f'\033[91mPor favor, digite um valor válido!\033[m')