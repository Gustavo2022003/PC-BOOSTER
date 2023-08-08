import os

username = os.getlogin()
__dirname = os.path.dirname(__file__)

def title(txt):
    print("\n")
    print('=' * (len(txt) + 4))
    print(f'  \033[107m\033[35m{txt}\033[m')
    print('=' * (len(txt) + 4))

def main():
    os.system("cls")
    title("PC BOOSTER/TOOLS V.1")
    print("\033[107m\033[95mFeito para meu amoreco <3\033[m\n")
    print("1 - Limpar arquivos temporários")
    print("2 - Mostrar diretório atual")
    print("3 - Mostrar informações do sistema")
    print("4 - Desligar/suspender")
    print("5 - Sair")
    user_input = int(input("Digite uma opção: "))
    if user_input == 1:
        menu_temp()
    elif user_input == 2:
        print("\nDiretório atual: ")
        print(f'\n\033[94m{__dirname}\033[m')
    elif user_input == 3:
        print("\n\033[92mInformações do sistema:\033[m")
        os.system("systeminfo")
    elif user_input == 4:
        desligar_suspender()
    elif user_input == 5:
        exit()
    else:
        print("\n\033[91mOpção inválida!\033[m")

def desligar_suspender():
    os.system("cls")
    time = int(input("Em quantos minutos você deseja desligar? [0] - voltar\n"))
    if time == 0:
        main()
    elif time > 0:
        os.system(f'shutdown -s -t {time * 60}')
    else:
        print("\n\033[91mOpção inválida!\033[m")

    

def menu_temp():
    os.system("cls")
    files_counter = 0
    print("0 - Tudo")
    print("1 - Prefetch")
    print("2 - Temp")
    print("3 - %temp%")
    print("4 - Voltar")
    user_input = int(input("Digite uma opção: "))

    if user_input == 0:

        files_initial = 0
        for file in os.listdir("C:\\Windows\\Prefetch"):
            files_initial += 1
        for file in os.listdir("C:\\Windows\\Temp"):
            files_initial += 1
        for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
            files_initial += 1

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

        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

        files_final = 0
        for file in os.listdir("C:\\Windows\\Prefetch"):
            files_final += 1
        for file in os.listdir("C:\\Windows\\Temp"):
            files_final += 1
        for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
            files_final += 1

        print(f'\n\033[92mDe {files_initial} arquivos, {files_initial - files_final} foram apagados com sucesso!\033[m')
        
        print("\n\033[93mArquivos restantes:\033[m")
        for files in os.listdir("C:\\Windows\\Prefetch"):
            print(f'\033[91m{files}\033[m')
        
        for files in os.listdir("C:\\Windows\\Temp"):
            print(f'\033[91m{files}\033[m')
        
        for files in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
            print(f'\033[91m{files}\033[m')

        print("\n\033[93mAtenção!\033[m\nAlguns arquivos não podem ser excluidos por conta que estão sendo utilizados por algum processo no momento.")

        input("\n\033[35mAperte ENTER para continuar...\033[m")

    elif user_input == 1:

        files_initial = 0
        for file in os.listdir("C:\\Windows\\Prefetch"):
            files_initial += 1

        try:
            for file in os.listdir("C:\\Windows\\Prefetch"):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do Prefetch
                os.system(f'del /s /q C:\\Windows\\Prefetch\\{file}')
                os.system(f'rmdir /s /q C:\\Windows\\Prefetch\\{file}')
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

        files_final = 0
        for file in os.listdir("C:\\Windows\\Prefetch"):
            files_final += 1

        print(f'\n\033[92mDe {files_initial} arquivos, {files_initial - files_final} foram apagados com sucesso!\033[m')
        
        print("\n\033[93mArquivos restantes:\033[m")
        for files in os.listdir("C:\\Windows\\Prefetch"):
            print(f'\033[91m{files}\033[m')

        print("\n\033[93mAtenção!\033[m\nAlguns arquivos não podem ser excluidos por conta que estão sendo utilizados por algum processo no momento.")

        input("\n\033[35mAperte ENTER para continuar...\033[m")

    elif user_input == 2:

        files_initial = 0
        for file in os.listdir("C:\\Windows\\Temp"):
            files_initial += 1

        try:
            for file in os.listdir("C:\\Windows\\Temp"):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do Temp
                os.system(f'del /s /q C:\\Windows\\Temp\\{file}')
                os.system(f'rmdir /s /q C:\\Windows\\Temp\\{file}')
                files_counter += 1
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

        files_final = 0
        for file in os.listdir("C:\\Windows\\Temp"):
            files_final += 1

        print(f'\n\033[92mDe {files_initial} arquivos, {files_initial - files_final} foram apagados com sucesso!\033[m')
        
        print("\n\033[93mArquivos restantes:\033[m")
        for files in os.listdir("C:\\Windows\\Temp"):
            print(f'\033[91m{files}\033[m')

        print("\n\033[93mAtenção!\033[m\nAlguns arquivos não podem ser excluidos por conta que estão sendo utilizados por algum processo no momento.")

        input("\n\033[35mAperte ENTER para continuar...\033[m")

    elif user_input == 3:

        files_initial = 0
        for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
            files_initial += 1

        try:
            for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
                print(f'Apagando arquivo: {file}')
                # Removendo todos arquivos e pastas do %temp%
                os.system(f'del /s /q C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                os.system(f'rmdir /s /q C:\\Users\\{username}\\AppData\\Local\\Temp\\{file}')
                files_counter += 1
        except Exception as error:
            print(f'\033[91mErro: {error}\033[m')

        files_final = 0
        for file in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
            files_final += 1

        print(f'\n\033[92mDe {files_initial} arquivos, {files_initial - files_final} foram apagados com sucesso!\033[m')
        
        print("\n\033[93mArquivos restantes:\033[m")
        for files in os.listdir(f'C:\\Users\\{username}\\AppData\\Local\\Temp'):
            print(f'\033[91m{files}\033[m')

        print("\n\033[93mAtenção!\033[m\nAlguns arquivos não podem ser excluidos por conta que estão sendo utilizados por algum processo no momento.")

        input("\n\033[35mAperte ENTER para continuar...\033[m")

    elif user_input == 4:
        main()

    else:
        print("\n\033[91mOpção inválida!\033[m")

while True:
    main()