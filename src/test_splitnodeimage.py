import unittest

from main import *

class testsplitnodeimage(unittest.TestCase):
    def test_split_single_img(self):
        text = TextNode("This is a text with an image ![to boot dev](https://www.boot.dev/image.jpg)", TextType.TEXT)
        split_text = split_nodes_image([text])
        expected = [
                    TextNode("This is a text with an image ", TextType.TEXT),
                    TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev/image.jpg")
        ]
        self.assertEqual(split_text, expected)

    def test_split_multiple_img(self):
        text = TextNode("This is a text with this image ![to boot dev](https://www.boot.dev/image.jpg) and another ![here](https://www.boot.dev/another.gif)", TextType.TEXT)
        split_text = split_nodes_image([text])
        expected = [
                    TextNode("This is a text with this image ", TextType.TEXT),
                    TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev/image.jpg"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode("here", TextType.IMAGE, "https://www.boot.dev/another.gif")
        ]
        self.assertEqual(split_text, expected)

    def test_split_img_with_trailing_text(self):
            text = TextNode("This is a text with this image ![to boot dev](https://www.boot.dev/image.jpg) and another ![here](https://www.boot.dev/another.gif) for your pleasure", TextType.TEXT)
            split_text = split_nodes_image([text])
            expected = [
                        TextNode("This is a text with this image ", TextType.TEXT),
                        TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev/image.jpg"),
                        TextNode(" and another ", TextType.TEXT),
                        TextNode("here", TextType.IMAGE, "https://www.boot.dev/another.gif"),
                        TextNode(" for your pleasure", TextType.TEXT)
            ]
            self.assertEqual(split_text, expected)

    def test_split_img_with_no_start_text(self):
            text = TextNode("![to boot dev](https://www.boot.dev/image.jpg) and another ![here](https://www.boot.dev/another.gif) for your pleasure", TextType.TEXT)
            split_text = split_nodes_image([text])
            expected = [
                        TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev/image.jpg"),
                        TextNode(" and another ", TextType.TEXT),
                        TextNode("here", TextType.IMAGE, "https://www.boot.dev/another.gif"),
                        TextNode(" for your pleasure", TextType.TEXT)
            ]
            self.assertEqual(split_text, expected)
            