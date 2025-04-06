import unittest

from main import *
from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("Hello, world!", TextType.TEXT)
        result = text_node_to_html_node(node)
        self.assertIsNone(result.tag)
        self.assertEqual(result.value, "Hello, world!")
    
    def test_bold_text(self):
        node = TextNode("Very bold.", TextType.BOLD)
        result = text_node_to_html_node(node)
        self.assertEqual(result.tag, "strong")
        self.assertEqual(result.children[0].value, "Very bold.")
    
    #def test_link_node(self):
    #    node = TextNode("Click me", TextType.LINK, "https://www.boot.dev")
    #    result = text_node_to_html_node(node)
    #    self.assertEqual(result.tag, "a")
    #    self.assertEqual(result.value, "Click me")
    #    self.assertEqual(result.props["href"], "https://www.boot.dev")
    
    #def test_image_node(self):
    #    node = TextNode("Alt text", TextType.IMAGE, "/img/pic.jpg")
    #    result = text_node_to_html_node(node)
    #    self.assertEqual(result.tag, "img")
    #    self.assertEqual(result.value, "")
    #    self.assertEqual(result.props["src"], "/img/pic.jpg")
    #    self.assertEqual(result.props["alt"], "Alt text")
