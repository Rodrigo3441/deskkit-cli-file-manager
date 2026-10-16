import pathlib

def verify_path(folder_path: str) -> None | pathlib.Path:
    if not folder_path:
        return None
    
    # check if the path exists
    if not pathlib.Path(folder_path).exists():
        return None
    
    # check if the path is a directory
    elif not pathlib.Path(folder_path).is_dir():
        return None

    return pathlib.Path(folder_path)


def list_everything_in_folder(verified_path: pathlib.Path) -> None | list:
    """
    return: Files and folders in the given path as one list of dictionaries.
    """
    if verified_path is None:
        return None

    folders = []
    files = []

    for file in verified_path.iterdir():
        if file.is_file():
            files.append(
                {
                    'modified_time': file.stat().st_mtime,
                    'size': file.stat().st_size,
                    'name': file.name
                }
            )

        elif file.is_dir():
            folders.append(
                {
                    'modified_time': file.stat().st_mtime,
                    'size': '',
                    'name': file.name
                }
            )

    results = folders + files
    return results


def return_total_files_per_extension(verified_path: pathlib.Path) -> None | dict:
    """
    return: Total files per extension in the given path as a dictionary.
    """
    if verified_path is None:
        return None

    extension_count = {}

    for file in verified_path.iterdir():
        if file.is_file():
            extension = file.suffix
            if extension in extension_count:
                extension_count[extension] += 1
            else:
                extension_count[extension] = 1

    return extension_count  

def return_files_inside_folder(verified_path: pathlib.Path) -> None | list:
    """
    return: Files in the given path as a list
    """

    if verified_path is None:
        return None

    files = []

    for file in verified_path.iterdir():
        if file.is_file():
            files.append(file.name)

    return files 