import os

def get_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    file_path = os.path.join(project_root, "files", filename)
    return file_path
