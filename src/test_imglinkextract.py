import unittest

from imglinkextract import *

class testimgurlextract(unittest.TestCase):
    def test_extract_one_img(self):
        text = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)")
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(text, expected)
    
    def test_extract_two_img(self):
        text = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(text, expected)
    
    def test_extract_one_link(self):
        text = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(text, expected)

    def test_extract_two_link(self):
        text = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(text, expected)

    def test_extract_empty_string(self):
        text = extract_markdown_images("")
        expected = []
        self.assertEqual(text, expected)
    
    def test_extract_regular_text(self):
        text = extract_markdown_images("This is just normal text")
        expected = []
        self.assertEqual(text, expected)

    def test_extract_with_special_char(self):
        text = extract_markdown_links("This is the search result: [search results](https://example.com/search?q=magic&type=spell)")
        expected = [("search results", "https://example.com/search?q=magic&type=spell")]
        self.assertEqual(text, expected)
