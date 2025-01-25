from textnode import *
from htmlnode import *
from imglinkextract import *
from node_parser import *
from html_converter import *
from markdown_converter import *

def main():
    test = TextNode("Testing", TextType.BOLD, "http://yadayada")
    print(test)

if __name__ == "__main__":
    main()