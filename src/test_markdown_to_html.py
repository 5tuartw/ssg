import unittest
from markdown_converter import *

class testmarkdowntohtml(unittest.TestCase):
    def test_paragraph_markdown_to_html(self):
        text = "This is just plain text so has no markdown"
        node = markdown_to_html_nodes(text)
        self.assertEqual(node.tag, "div")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[0].children[0].value, "This is just plain text so has no markdown")

        # Test multiple paragraphs
        node = markdown_to_html_nodes("First paragraph\n\nSecond paragraph")
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[1].tag, "p")

        node = markdown_to_html_nodes("")
        self.assertEqual(len(node.children), 0)

        node = markdown_to_html_nodes("\n\n")
        self.assertEqual(len(node.children), 0)

    def test_headings(self):
        # Test single heading
        node = markdown_to_html_nodes("# Heading 1")
        self.assertEqual(node.children[0].tag, "h1")

        # Test multiple heading levels
        node = markdown_to_html_nodes("# Heading 1\n\n### Heading 3")
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[1].tag, "h3")
    
    def test_headings_and_paragraphs(self):
        node = markdown_to_html_nodes("# Heading 1\n\nWith a paragraph of text underneath")
        self.assertEqual(node.children[0].tag, "h1")
        self.assertEqual(node.children[1].tag, "p")

    def test_headings_with_formatting(self):
        node = markdown_to_html_nodes("# Heading with **bold** and *italic* text")
        node = markdown_to_html_nodes("# Heading with **bold** and *italic* text")
        self.assertEqual(len(node.children[0].children), 5)
        self.assertEqual(node.children[0].children[1].tag, "strong")
        self.assertEqual(node.children[0].children[3].tag, "em")

    def test_quote_with_paragraphs_and_formatting(self):
        markdown = "> This is **bold** text\n>\n> This is *italic* text"
        node = markdown_to_html_nodes(markdown)
        
        # Check we have a blockquote node
        quote_node = node.children[0]
        self.assertEqual(quote_node.tag, "blockquote")
        
        # Check we have 2 paragraphs
        self.assertEqual(len(quote_node.children), 2)
        self.assertEqual(quote_node.children[0].tag, "p")
        self.assertEqual(quote_node.children[1].tag, "p")
        
        # Check first paragraph has bold
        first_p = quote_node.children[0]
        self.assertEqual(len(first_p.children), 3)  # text, bold, text
        self.assertEqual(first_p.children[1].tag, "strong")
        
        # Check second paragraph has italic
        second_p = quote_node.children[1]
        self.assertEqual(len(second_p.children), 3)  # text, italic, text
        self.assertEqual(second_p.children[1].tag, "em")

    def test_simple_quote(self):
        markdown = "> This is a quote"
        node = markdown_to_html_nodes(markdown)
        self.assertIsNotNone(node.children)
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "blockquote")

    def test_unordered_list(self):
        text = "* This\n* Is\n * A\n* List"
        node = markdown_to_html_nodes(text)
        self.assertEqual(len(node.children[0].children), 4)

        text = "* This\n* Is\n* A\n* **Bold**\n* List"
        node = markdown_to_html_nodes(text)
        self.assertEqual(len(node.children[0].children), 5)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item\n3. Third item"
        node = o_list_to_node(markdown)
        self.assertEqual(node.tag, "ol")
        self.assertEqual(len(node.children), 3)
        self.assertEqual(node.children[0].tag, "li")
        self.assertEqual(node.children[0].children[0].value, "First item")
    
    def test_code_block(self):
        markdown = "```\ndef test():\n    pass\n```"
        node = code_to_node(markdown)
        self.assertEqual(node.tag, "pre")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "code")
        self.assertEqual(node.children[0].children[0].value, "def test():\n    pass")