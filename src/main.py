from generate_page import generate_pages_recursive
import os
from io_operation import copy_recursive, delete_directory_dst

def main():
    current_directory = os.path.dirname(__file__)
    project_root = os.path.dirname(current_directory)

    static_path = os.path.join(project_root, "static")
    public_path = os.path.join(project_root, "public")

    delete_directory_dst(public_path)
    copy_recursive(static_path, public_path)
    generate_pages_recursive("content", "template.html", "public")
    




if __name__ == "__main__":
    main()
