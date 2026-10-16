from src.helper_functions import verify_path
from src.organize_files import organize_files_by_extension


def organize_files(verified_path):
    print(f'Files in this directory will be moved into subfolders according to their extensions. Continue? (yes/no)')
    option = input().strip().lower()

    if option == 'yes':
        organize_files_by_extension(verified_path)
        return

    print('Nothing changed')


def main():
    while True:
        folder_path = input('Enter the folder path you want to perform operations: ').strip()
        verified_path = verify_path(folder_path)

        if verified_path:
            break

        print('The entered folder is not valid, please check your folder path.')


    while True:
        print('=' * 50)
        print(f'Current selected folder: {verified_path}\n')  
        print('1- Organize folder files by extension')  
        print('2- Exit')
        print('=' * 50)

        option = input().strip()

        match option:
            case '1':
                organize_files(verified_path)

            case '2':
                exit(0)
            case _:
                print('Invalid option')

main()
