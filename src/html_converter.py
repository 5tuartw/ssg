from textnode import *
from htmlnode import *

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
            return HTMLNode(None, text)
        case TextType.BOLD:
            return HTMLNode("b", text)
        case TextType.ITALIC:
            return HTMLNode("i", text)
        case TextType.CODE:
            return HTMLNode("code", text)
        case TextType.LINK:
            return HTMLNode("a", text,{"href": url})
        case TextType.IMAGE:
            return HTMLNode("img", "", {"src": url, "alt": text})
        case _:
            raise Exception("Invalid text type")
