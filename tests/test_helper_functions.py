import pathlib
from src.helper_functions import (
    verify_path,
    list_everything_in_folder,
    return_total_files_per_extension,
    return_files_inside_folder
)

VALID_PATH = 'C:\\Users\\Rodrigo\\Downloads'
NON_EXISTENT_PATH = 'C:\\Users\\Rodrigo\\NonExistentFolder'
EMPTY_PATH = ''

def test_verify_path():
    # Test with a valid directory path
    assert verify_path(VALID_PATH) == pathlib.Path(VALID_PATH)

    # Test with a non-existent path
    assert verify_path(NON_EXISTENT_PATH) is None

    # Test with an empty string]
    assert verify_path(EMPTY_PATH) is None

def test_list_everything_in_folder():
    # Test with a valid directory path
    valid_path = VALID_PATH
    verified_path = verify_path(valid_path)
    result = list_everything_in_folder(verified_path)
    assert isinstance(result, list)

    # Test with a non-existent path
    invalid_path = NON_EXISTENT_PATH
    verified_invalid_path = verify_path(invalid_path)
    result_invalid = list_everything_in_folder(verified_invalid_path)
    assert result_invalid is None

    # Test with an empty string
    empty_path = EMPTY_PATH
    verified_empty_path = verify_path(empty_path)
    result_empty = list_everything_in_folder(verified_empty_path)
    assert result_empty is None

def test_return_total_files_per_extension():
    # Test with a valid directory path
    valid_path = VALID_PATH
    verified_path = verify_path(valid_path)
    result = return_total_files_per_extension(verified_path)
    assert isinstance(result, dict)

    # Test with a non-existent path
    invalid_path = NON_EXISTENT_PATH
    verified_invalid_path = verify_path(invalid_path)
    result_invalid = return_total_files_per_extension(verified_invalid_path)
    assert result_invalid is None

    # Test with an empty string
    empty_path = EMPTY_PATH
    verified_empty_path = verify_path(empty_path)
    result_empty = return_total_files_per_extension(verified_empty_path)
    assert result_empty is None

def test_return_files_inside_folder():
    # Test with a valid directory path
    valid_path = VALID_PATH
    verified_path = verify_path(valid_path)
    result = return_files_inside_folder(verified_path)
    assert isinstance(result, list)

    # Test with a non-existent path
    invalid_path = NON_EXISTENT_PATH
    verified_invalid_path = verify_path(invalid_path)
    result_invalid = return_files_inside_folder(verified_invalid_path)
    assert result_invalid is None

    # Test with an empty string
    empty_path = EMPTY_PATH
    verified_empty_path = verify_path(empty_path)
    result_empty = return_files_inside_folder(verified_empty_path)
    assert result_empty is None