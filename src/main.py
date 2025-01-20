from textnode import *
from htmlnode import *
from imglinkextract import *

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        old_node_text = old_node.text

        if old_node.text_type.value != "text":
            new_nodes.append(old_node)
        elif old_node_text.count(delimiter) % 2 != 0:
            raise Exception("Cannot split node with uneven delimiters.")
        else:

            current_text = ""
            normal_text = True
            i = 0

            while i < len(old_node_text):
                if len(delimiter) == 1:
                    char = old_node_text[i]
                    if char == delimiter and normal_text:
                        if current_text != "":
                            new_nodes.append(TextNode(current_text, TextType.TEXT))
                        normal_text = False
                        current_text = ""
                        i += 1
                    elif char == delimiter:
                        if current_text != "":
                            new_nodes.append(TextNode(current_text, text_type))
                        normal_text = True
                        current_text = ""
                        i += 1
                    else:
                        current_text += char
                        i += 1
                elif len(delimiter) == 2:
                    char = old_node_text[i]
                    chars = old_node_text[i:i+2]
                    if chars == delimiter and normal_text:
                        if current_text != "":
                            new_nodes.append(TextNode(current_text, TextType.TEXT))
                        normal_text = False
                        current_text = ""
                        i += 2
                    elif chars == delimiter:
                        if current_text != "":
                            new_nodes.append(TextNode(current_text, text_type))
                        normal_text = True
                        current_text = ""
                        i += 2
                    else:
                        current_text += char
                        i += 1
            
            if current_text != "":
                new_nodes.append(TextNode(current_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        old_node_text = old_node.text
        #print(f"The old text is: {old_node_text}")
        extracted_images = extract_markdown_images(old_node_text)
        #print(f"Images extracted: {extracted_images}")
        for extracted_image in extracted_images:
            alt_text = extracted_image[0]
            image_url = extracted_image[1]
            this_split = old_node_text.split(f"![{alt_text}]({image_url})",1)
            if this_split[0] != "":
                new_nodes.append(TextNode(this_split[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            old_node_text = this_split[1]
        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        old_node_text = old_node.text
        #print(f"The old text is: {old_node_text}")
        extracted_links = extract_markdown_links(old_node_text)
        #print(f"Links extracted: {extracted_links}")
        for extracted_link in extracted_links:
            link_text = extracted_link[0]
            link_url = extracted_link[1]
            this_split = old_node_text.split(f"[{link_text}]({link_url})",1)
            #print(f"The current splits are: {this_split}")
            if this_split[0] != "":
                new_nodes.append(TextNode(this_split[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            old_node_text = this_split[1]
        if old_node_text != "":
            new_nodes.append(TextNode(old_node_text, TextType.TEXT))
    
    return new_nodes

if __name__ == "__main__":
    main()