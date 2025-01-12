import unittest

from htmlnode import HTMLNode, LeafNode

class testleafnode(unittest.TestCase):
    def test_tag_no_props(self):
        leafnode = LeafNode("p", "This is a paragraph.")

        self.assertEqual(leafnode.tag, "p")
        self.assertEqual(leafnode.value, "This is a paragraph.")
        self.assertEqual(leafnode.props, None)

        htmlstring = leafnode.to_html()
        expected = "<p>This is a paragraph.</p>"
        self.assertEqual(expected, htmlstring)
    
    def test_tag_with_one_prop(self):
        leafnode = LeafNode("a", "This is a link", {"href": "https://www.google.com/", "target": "a place"})

        self.assertEqual(leafnode.props, {"href": "https://www.google.com/", "target": "a place"})

        htmlstring = leafnode.to_html()
        expected = '<a href="https://www.google.com/" target="a place">This is a link</a>'
        self.assertEqual(htmlstring, expected)
    
    def test_leaf_with_no_value(self):
        with self.assertRaises(ValueError):
            leaf = LeafNode("p", None)
            leaf.to_html()
    
        with self.assertRaises(ValueError):
            leaf = LeafNode("p", "")
            leaf.to_html()
    
    def test_no_tag(self):
        leaf = LeafNode(None, "raw text")
        self.assertEqual(leaf.to_html(), "raw text")
    
    def test_empty_props(self):
        leaf = LeafNode("p", "text", {})
        self.assertEqual(leaf.to_html(), "<p>text</p>")
    
    def test_leaf_node_special_chars(self):
        # Test HTML special characters
        leaf = LeafNode("p", "Text with < and > symbols")
        self.assertEqual(leaf.to_html(), "<p>Text with < and > symbols</p>")
    
        # Test quotes in attributes
        leaf = LeafNode("div", "Some text", {"data-test": "value's \"quote\""})
        self.assertEqual(leaf.to_html(), '<div data-test="value\'s &quot;quote&quot;">Some text</div>')
        
        # Test multiple special characters
        leaf = LeafNode("span", "A & B & C")
        self.assertEqual(leaf.to_html(), "<span>A & B & C</span>")