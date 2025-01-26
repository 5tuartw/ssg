from markdown_converter import *
from html_converter import *
from extract_header import *

import os

def generate_page(from_path, template_path, dest_path):
    #print(f"Attempting to generate page from {from_path} to {dest_path} using {template_path}")
    try:
        with open(from_path, "r") as source_file:
            source_markdown = source_file.read()
        with open(template_path, "r") as template_file:
            template = template_file.read()
    except FileNotFoundError:
        print("Unable to open source or template file.")
        return
    except Exception as e:
        print(f"Error reading source or template: {e}")
        return

    html_nodes = markdown_to_html_nodes(source_markdown)
    html = html_nodes.to_html()
    title = extract_title(from_path)
    #print(f"Found header: {title}")

    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html)
      
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        with open(dest_path, "w") as dest_file:
            dest_file.write(final_html)
    except Exception as e:
        print(f"Unable to create destination file: {e}")
        return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    try:
        content_list = os.listdir(dir_path_content)
    except Exception as e:
        raise Exception(f"Could not list directory: {dir_path_content} ({e})")

    for item in content_list:
        item_path = os.path.join(dir_path_content, item)

        if os.path.isfile(item_path):
            item_name_split = item.split(".")
            item_name = "".join(item_name_split[:-1])
            item_ext = item_name_split[-1]
            if item_ext == "md":
                generate_page(item_path, "template.html", os.path.join(dest_dir_path, item_name+".html"))

        elif os.path.isdir(item_path):
            new_dest_dir = os.path.join(dest_dir_path, item)
            if not os.path.exists(new_dest_dir):
                os.mkdir(new_dest_dir)
            generate_pages_recursive(item_path, template_path, new_dest_dir)


