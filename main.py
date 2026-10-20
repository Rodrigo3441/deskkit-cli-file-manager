import questionary
from datetime import datetime
from pathlib import Path
from src.helper_functions import (
    verify_path,
    list_everything_in_folder
)
from src.organize_files import organize_files_by_extension


def read_folder_from_user() -> Path:
    while True:
        folder_path = questionary.text('Enter the folder path you want to perform operations: ').ask()
        verified_path = verify_path(folder_path)

        if verified_path:
            break

        elif not verified_path:
            print('No path was specified')
            return

        print('The entered folder is not valid, please check your folder path.')

    return verified_path


def organize_files(verified_path):
    option = questionary.confirm(
        'Files in this directory will be moved into subfolders according to their extensions. Continue?',
        default=False
    ).ask()

    if option:
        organize_files_by_extension(verified_path)
        return

    print('Nothing changed')


def print_folder_report(verified_path):
    results = list_everything_in_folder(verified_path)
    print('\n')

    if not results:
        print('The current folder is empty')
        return
    
    for result in results:
        last_mod_date = result['modified_date']
        date = datetime.fromtimestamp(last_mod_date)
        size_mb = round(result['size']/1_024_576, 2) if result['size'] != '' else ''
        size_mb = str(size_mb) + ' MB' if size_mb != '' else ''

        print(f"{date.strftime('%m/%d/%Y %I:%M:%S %p'):<25}{result['type']:<10}{size_mb:<16}{result['name']:<50}")


def main():
    verified_path = Path.cwd()

    CHOICES = {
        'Organize folder files by extension': lambda: organize_files(verified_path),
        'Show all files and folder within the specified path': lambda: print_folder_report(verified_path),
        'Exit': None
    }

    try:
        while True:
            print(f'\n\nCurrent selected folder: {verified_path}\n')  

            option = questionary.select(
                        'What do you want to do?',
                        choices=CHOICES.keys()
                    ).ask()

            if not option:
                return

            if option == 'Exit':
                return
            
            else:
                CHOICES[option]()        

    except KeyboardInterrupt:
        print('Action cancelled by the user')
        return


main()
