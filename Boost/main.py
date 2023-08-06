import os

__dirname = os.path.dirname(__file__)
files_counter = 0
username = os.getlogin()

def title(txt):
    print("\n")
    print('=' * (len(txt) + 4))
    print(f'  \033[92m{txt}\033[m')
    print('=' * (len(txt) + 4))

title("Bem vindo ao PC BOOSTER!")
print("1 - Apagar arquivos temporários")
print("2 - Mostrar diratório atual")
print("3 - Sair\n")
user_option = int(input("Digite a opção: "))

while user_option != 3:

    if user_option == 1:
        user_option_arquivos = int(input("\n1 - Prefetch\n2 - Temp\n3 - %temp%\n4 - Voltar\nDigite a opção: "))

        # Prefetch
        if user_option_arquivos == 1:
            try:
                for file in os.listdir("C:\\Windows\\Prefetch"):
                    print(f'Apagando arquivo: {file}')
                    os.system(f'del C:\\Windows\\Prefetch\\{file}')
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
                    os.system(f'del C:\\Windows\\Temp\\{file}')
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
                    os.system(f'del C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                    files_counter += 1
                print(f'\033[92m{files_counter} arquivos apagados com sucesso!\033[m')
                break
            except Exception as error:
                print(f'\033[91mErro: {error}\033[m')
        
        # Voltar
        if user_option_arquivos == 4:
            title("Bem vindo ao PC BOOSTER!")
            print("1 - Apagar arquivos temporários")
            print("2 - Mostrar diratório atual")
            print("3 - Sair\n")
            user_option = int(input("Digite a opção: "))

    # Mostrar diretório atual
    if user_option == 2:
        print("\nDiretório atual: ")
        print(f'\n\033[94m{__dirname}\033[m')
        title("Bem vindo ao PC BOOSTER!")
        print("1 - Apagar arquivos temporários")
        print("2 - Mostrar diratório atual")
        print("3 - Sair\n")
        user_option = int(input("Digite a opção: "))

    # Sair
    if user_option == 3:
        print("\033[93mSaindo...\033[m")
        break
else:
    print("\033[93mSaindo...\033[m")
    exit()