import os


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
    Return a tuple of (number_of_directories, number_of_files)
    """
    number_of_directories = 0
    number_of_files = 0

    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_dir():
                number_of_directories += 1
                subdir_result = count_dirs_and_files(entry.path)
                if subdir_result is not None:
                    number_of_directories += subdir_result[0]
                    number_of_files += subdir_result[1]

            if entry.is_file():
                number_of_files += 1

    return (number_of_directories, number_of_files)
