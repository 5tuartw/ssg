from textnode import *
from htmlnode import *

def main():
    test = TextNode("Testing", TextType.BOLD, "http://yadayada")
    print(test)

def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    url = text_node.url

    #TEXT = "text"
    #BOLD = "bold"
    #ITALIC = "italic"
    #CODE = "code"
    #LINK = "link"
    #IMAGE = "image"

    match text_type:
        case TextType.TEXT:
            return LeafNode(None, text)
        case TextType.BOLD:
            return LeafNode("b", text)
        case TextType.ITALIC:
            return LeafNode("i", text)
        case TextType.CODE:
            return LeafNode("code", text)
        case TextType.LINK:
            return LeafNode("a", text,{"href": url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": url, "alt": text})
        case _:
            raise Exception("Invalid text type")


if __name__ == "__main__":
    main()