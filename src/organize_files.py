import pathlib
from src.helper_functions import (
    return_files_inside_folder
)

def organize_files_by_extension(verified_path: pathlib.Path) -> None:
    """
    Organizes files in the given path into subfolders based on their extensions.

    For each file, it creates a subfolder inside the current folder named as the file extension,
    if there's a file with the same name inside the destination folder, it renames the current file to make
    sure there will be no replacings
    """
    if verified_path is None:
        return

    total_moved_files = 0
    total_failed_files = 0

    for file in verified_path.iterdir():
        if file.is_file():
            extension = file.suffix[1:]  # Get the extension without the dot

            try:
                # If the file has no extension, create a folder named 'no_extension'
                if not extension:  
                    new_folder = verified_path / 'no_extension'
                    new_folder.mkdir(exist_ok=True)
                else:
                    # Create a new folder for the extension if it doesn't exist
                    new_folder = verified_path / extension
                    new_folder.mkdir(exist_ok=True)

            
                # If a file with the same name already exists in the new folder, rename the file
                if (new_folder / file.name).exists():
                    base_name = file.stem
                    counter = 1

                    while True:
                        new_file_name = f'{base_name}_{counter}{file.suffix}'
                        new_file_path = new_folder / new_file_name

                        if not new_file_path.exists():
                            break
                        counter += 1
                    # Move the file to the new folder with the new name
                    file.rename(new_file_path)
                    print(f'renamed \'{file.name}\' to \'{new_file_name}\'\nmoved \'{new_file_name}\' into \'{new_folder}\'')

                else:
                    # Move the file to the new folder
                    new_file_path = new_folder / file.name
                    file.rename(new_file_path)
                    print(f'moved \'{file.name}\' into \'{new_folder}\'')

                total_moved_files += 1
                

            # Skip the file if there's an error, such as permission issues or if the file is in use
            except OSError as e:
                total_failed_files += 1
                print(f'failed to move the file \'{file.name}\': {e.strerror}')

    print()

    if total_moved_files == 0 and total_failed_files == 0:
        print('No files have been moved: the folder has no files to organize.')

    elif total_moved_files > 0 and total_failed_files == 0:
        print('All the files have been moved successfully.')

    elif total_moved_files == 0 and total_failed_files > 0:
        print('No files have been moved.')

    else:
        print('Some files failed to move during the process')

    print(f'Total moved files: {total_moved_files} | Total failed files: {total_failed_files}')
        
