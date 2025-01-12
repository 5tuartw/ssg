import unittest

from htmlnode import HTMLNode

class testhtmlnode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")
    
    def test_default_parameters(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_full_parameters(self):
        node= HTMLNode(
            tag = "p",
            value = "Hello, World!",
            children = [HTMLNode(value="Child node")],
            props = {"class": "greeting"}
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value,"Hello, World!")
        self.assertEqual(node.children[0].value, "Child node")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.props, {"class": "greeting"})
    
    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr_method(self):
        node = HTMLNode(
            tag = "a",
            value = "Click me",
            props = {"href":"https://www.google.com/"}
        )
        expected_repr = 'Tag: a, Value: Click me, Children: None, Props:  href="https://www.google.com/"'
        self.assertEqual(repr(node), expected_repr)