from textnode import *
from htmlnode import *
from imglinkextract import *
from node_parser import *
from html_converter import *
from markdown_converter import *
from generate_page import *

import os
import shutil
import logging

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
src_static = os.path.join(project_root, "static")
dest_public = os.path.join(project_root, "public")

logging.basicConfig(
    filename = "actions.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def clear_public_dir():
    try:
        if os.path.exists(dest_public):
            logging.info("Removing directory: public")
            shutil.rmtree(dest_public)
            logging.info("Removed directory: public")
        os.mkdir(dest_public)
        logging.info("Created directory: public")
    except FileNotFoundError:
        logging.warning("Tried to remove public, but dir not found. Creating directory.")
        os.mkdir(dest_public)
        logging.info("Created directory: public")
    except Exception as e:
        logging.error(f"An error occurred while clearing the public directory: {e}")
        print(f"An error occurred while clearing the public directory: {e}")

def copy_static_to_public(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            logging.info(f"Copying file: {source_path} to {destination_path}")
            shutil.copy(source_path, destination_path)
        elif os.path.isdir(source_path):
            logging.info(f"Entering directory: {source_path}")
            copy_static_to_public(source_path, destination_path)
    
def main():
    clear_public_dir()
    copy_static_to_public(src_static, dest_public)
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()