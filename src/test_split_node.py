import unittest

from main import *
from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_parser import *

class TestSplitNodeDelimiter(unittest.TestCase):

    def test_split_node_single(self):
        node = TextNode("Hello, *great* world!", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(result, [
                                        TextNode("Hello, ",TextType.TEXT),
                                        TextNode("great", TextType.BOLD),
                                        TextNode(" world!", TextType.TEXT)])
    
    def test_split_node_double(self):
        node1 = TextNode("Hello, `great coding` world!", TextType.TEXT)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(result, [
                                    TextNode("Hello, ",TextType.TEXT),
                                    TextNode("great coding", TextType.CODE),
                                    TextNode(" world!", TextType.TEXT),
                                    TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT)
        ])
    
    def test_split_unpaired_delim(self):
        node = TextNode("Hello, *great* world!*", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(str(context.exception),"Cannot split node with uneven delimiters.")
    
    def test_nonmatching_delimiters(self):
        node1 = TextNode("Hello, *great coding* world!", TextType.TEXT)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(result, [
                                    TextNode("Hello, *great coding* world!", TextType.TEXT),
                                    TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT)
        ])
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Hello, *great coding* world!")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "This is text with a ")
        self.assertEqual(result[1].text_type, TextType.TEXT)
        self.assertEqual(result[2].text, "code block")
        self.assertEqual(result[2].text_type, TextType.CODE)
        self.assertEqual(result[3].text, " word")
        self.assertEqual(result[3].text_type, TextType.TEXT)
    
    def test_multiple_delimiters(self):
        node = TextNode("Here is `some code` and `more code` in one line", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
                                    TextNode("Here is ", TextType.TEXT),
                                    TextNode("some code", TextType.CODE),
                                    TextNode(" and ", TextType.TEXT),
                                    TextNode("more code", TextType.CODE),
                                    TextNode(" in one line", TextType.TEXT)
        ])

    def test_consecutive_delimiters(self):
        node = TextNode("text``more text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
                                TextNode("text", TextType.TEXT),
                                TextNode("more text", TextType.TEXT)
        ])
    
    def test_two_char_delimiter(self):
        node = TextNode("Hello, **great** world!", TextType.TEXT)
        #print("\nDebug test_two_char_delimiter:") 
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        #print(f"Result: {result}")
        self.assertEqual(result, [
                                    TextNode("Hello, ",TextType.TEXT),
                                    TextNode("great", TextType.BOLD),
                                    TextNode(" world!", TextType.TEXT)])
    
    def test_start_and_end_delims(self):
        node = TextNode("**Hello**, great **world!**", TextType.TEXT)
        #print("\nDebug test_two_char_delimiter:") 
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        #print(f"Result: {result}")
        self.assertEqual(result, [
                                    TextNode("Hello",TextType.BOLD),
                                    TextNode(", great ", TextType.TEXT),
                                    TextNode("world!", TextType.BOLD)])
    
    def test_mixed_count_delims(self):
        node = TextNode("**Hello**, *great* **world!**", TextType.TEXT)
        #print("\nDebug test_two_char_delimiter:") 
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        #print(f"Result: {result}")
        self.assertEqual(result, [
                                    TextNode("Hello",TextType.BOLD),
                                    TextNode(", *great* ", TextType.TEXT),
                                    TextNode("world!", TextType.BOLD)])