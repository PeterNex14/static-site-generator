from markdown_extractor import extract_title
from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as from_file:
        content = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()

    title = extract_title(content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path) and from_path.endswith(".md"):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        elif os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path, basepath)