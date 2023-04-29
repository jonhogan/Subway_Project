"""
This module contains a function to get the path to a file in the files directory.

  Parameters:
    file_name (str): The name of the file

  Returns:
    str: The path to the file

"""

import os

def get_file_path(filename):
    """
    Get the path to a file in the files directory.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    file_path = os.path.join(project_root, "files", filename)
    return file_path
