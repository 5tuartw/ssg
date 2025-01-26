from textnode import *
from htmlnode import *
from imglinkextract import *
from node_parser import *
from html_converter import *
from markdown_converter import *
import os

if os.path.exists("../static"):
    print("The 'static' directly exists!")
else:
    print("No sign of the 'static' dir here.")


def main():
    test = TextNode("Testing", TextType.BOLD, "http://yadayada")
    print(test)

if __name__ == "__main__":
    main()