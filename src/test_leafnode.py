import unittest

from htmlnode import HTMLNode, LeafNode

class testleafnode(unittest.TestCase):
    def test_leaf_with_no_value(self):
        with self.assertRaises(ValueError):
            leaf = LeafNode("")
            leaf.to_html()
    
        with self.assertRaises(ValueError):
            leaf = LeafNode(None)
            leaf.to_html()
    
    def test_leaf_node_special_chars(self):
        # Test HTML special characters
        leaf = LeafNode("Text with < and > symbols")
        self.assertEqual(leaf.to_html(), "Text with < and > symbols")
    
        # Test quotes in attributes
        #leaf = LeafNode("Some text", {"data-test": "value's \"quote\""})
        #self.assertEqual(leaf.to_html(), '<div data-test="value\'s &quot;quote&quot;">Some text</div>')
        
        # Test multiple special characters
        #leaf = LeafNode("span", "A & B & C")
        #self.assertEqual(leaf.to_html(), "<span>A & B & C</span>")