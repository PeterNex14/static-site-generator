import sys
from generate_page import generate_pages_recursive
import os
import sys
from io_operation import copy_recursive, delete_directory_dst

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    current_directory = os.path.dirname(__file__)
    project_root = os.path.dirname(current_directory)

    static_path = os.path.join(project_root, "static")
    docs_path = os.path.join(project_root, "docs")
    content_path = os.path.join(project_root, "content")
    template_path = os.path.join(project_root, "template.html")


    delete_directory_dst(docs_path)
    copy_recursive(static_path, docs_path)
    generate_pages_recursive(content_path, template_path, docs_path, basepath)
    




if __name__ == "__main__":
    main()
