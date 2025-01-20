import unittest

from main import *

class testsplitnodelink(unittest.TestCase):
    def test_split_single_link(self):
        text = TextNode("This is a text with a link [to boot dev](https://www.boot.dev/)", TextType.TEXT)
        split_text = split_nodes_link([text])
        expected = [
                    TextNode("This is a text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev/")
        ]
        self.assertEqual(split_text, expected)

    def test_split_multiple_links(self):
        text = TextNode("This is a text with this link [to boot dev](https://www.boot.dev/image.jpg) and another [here](https://www.boot.dev/another.gif)", TextType.TEXT)
        split_text = split_nodes_link([text])
        expected = [
                    TextNode("This is a text with this link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev/image.jpg"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode("here", TextType.LINK, "https://www.boot.dev/another.gif")
        ]
        self.assertEqual(split_text, expected)