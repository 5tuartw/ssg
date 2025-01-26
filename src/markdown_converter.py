from htmlnode import *
from node_parser import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped = [block.strip() for block in blocks]
    return stripped

def block_to_block_type(block):
    heading_starters = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(heading_starters):
        return "heading"
    if block[:3] == block[-3:] == "```":
        return "code"
    if block.startswith(">"):
        is_valid_quote = True
        for line in block.split("\n"):
            is_valid_quote = line.startswith(">")
            if not is_valid_quote:
                break
        if is_valid_quote:
            return "quote"
    ulist_starters = ("* ", "- ")
    if block.startswith(ulist_starters):
        is_valid_ulist = True
        for line in block.split("\n"):
            is_valid_ulist = line.startswith(ulist_starters)
            if not is_valid_ulist:
                break
        if is_valid_ulist:
            return "unordered_list"
    if block.startswith("1. "):
        number = 1
        is_valid_olist = True
        split_list = block.split("\n")
        for line in split_list:
            is_valid_olist = line.startswith(str(number)+". ")
            if not is_valid_olist:
                break
            number += 1
        if is_valid_olist:
            return "ordered_list"
    return "paragraph"

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    nodes = []
    for text_node in text_nodes:
        node = text_node_to_html_node(text_node)
        nodes.append(node)
    return nodes

def create_bold_node(text):
    child = LeafNode(text)
    return HTMLNode(tag="strong", children = [child])

def create_italic_node(text):
    child = LeafNode(text)
    return HTMLNode(tag="em", children = [child])

def create_code_node(text):
    child = LeafNode(text)
    return HTMLNode(tag="code", children = [child])

def create_text_node(text):
    return LeafNode(text)

def text_node_to_html_node(text_node):
    t_type = text_node.text_type
    if t_type == TextType.BOLD:
        return create_bold_node(text_node.text)
    if t_type == TextType.ITALIC:
        return create_italic_node(text_node.text)
    if t_type == TextType.CODE:
        return create_code_node(text_node.text)
    if t_type == TextType.TEXT:
        return LeafNode(text_node.text)
    raise Exception("Cannot create html node for unknown text type")
    
def paragraph_to_node(text):
    node = HTMLNode(tag="p")
    node.children = text_to_children(text)
    return node

def heading_to_node(text):
    [heading_prefix, heading] = text.split(" ",1)
    level = len(heading_prefix)
    node = HTMLNode(tag=f"h{level}")
    node.children = text_to_children(heading)
    return node

def quoteblock_to_node(text):
    lines = "".join(text.split(">"))
    node = HTMLNode(tag="blockquote")
    paragraphs = lines.split("\n\n")
    node.children = [paragraph_to_node(p) for p in paragraphs]
    return node

def u_list_to_node(text):
    items = text.split("\n")
    node = HTMLNode(tag="ul", children = [])
    for item in items:
        item_text = item[2:]
        item_node = HTMLNode(tag="li")
        item_node.children = text_to_children(item_text)
        node.children.append(item_node)
    return node

def o_list_to_node(text):
    items = text.split("\n")
    node = HTMLNode(tag="ol", children = [])
    for item in items:
        item_text = item.split(" ",1)[1]
        item_node = HTMLNode(tag="li")
        item_node.children = text_to_children(item_text)
        node.children.append(item_node)
    return node

def code_to_node(text):
    text = text[3:-3].strip()
    prenode = HTMLNode(tag = "pre")
    code_node = HTMLNode(tag="code", children = [LeafNode(text)])
    prenode.children = [code_node]
    return prenode

def markdown_to_html_nodes(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph" and block.strip():
            html_nodes.append(paragraph_to_node(block))
        if block_type == "heading":
            html_nodes.append(heading_to_node(block))
        if block_type == "quote":
            html_nodes.append(quoteblock_to_node(block))
        if block_type == "unordered_list":
            html_nodes.append(u_list_to_node(block))
        if block_type == "ordered_list":
            html_nodes.append(o_list_to_node(block))

    
    parent = HTMLNode(tag = "div", children = html_nodes)

    return parent