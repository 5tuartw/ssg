import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class testleafnode(unittest.TestCase):

    #Test cases:
    #parent nodes without children/tags (Value errors)
    #parent node with empty children list
    #parent node with one child, no properties
    #parent node with one child, one property
    #parent node with one child, multiple properties
    #parent node with multiple children
    #parent node with parent node as child
    #parent node with parent and child as children


    def test_parent_no_child(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("p", None)
            parent.to_html()
    
    def test_parent_no_tags(self):
        leafnode = LeafNode("This is a paragraph.")

        with self.assertRaises(ValueError):
            parent = ParentNode(None, [leafnode])
            parent.to_html()
    
    def test_parent_one_child(self):
        leafnode = LeafNode("This is a paragraph.")

        parent = ParentNode("b",[leafnode])

        self.assertEqual(parent.tag, "b")
        self.assertEqual(parent.children, [leafnode])
        self.assertEqual(parent.props, None)

        htmlstring = parent.to_html()
        expected = "<b>This is a paragraph.</b>"
        self.assertEqual(expected, htmlstring)


    def test_parent_with_property(self):
        leafnode = LeafNode("This is a paragraph.")

        parent = ParentNode("b",[leafnode],{"thing": "this"})

        self.assertEqual(parent.tag, "b")
        self.assertEqual(parent.children, [leafnode])
        self.assertEqual(parent.props, {"thing": "this"})

        htmlstring = parent.to_html()
        expected = '<b thing="this">This is a paragraph.</b>'
        self.assertEqual(expected, htmlstring)
    
    def test_parent_with_properties(self):
        leafnode = LeafNode("This is a paragraph.")

        parent = ParentNode("b",[leafnode],{"thing": "this", "other": "that"})

        self.assertEqual(parent.tag, "b")
        self.assertEqual(parent.children, [leafnode])
        self.assertEqual(parent.props, {"thing": "this", "other": "that"})

        htmlstring = parent.to_html()
        expected = '<b thing="this" other="that">This is a paragraph.</b>'
        self.assertEqual(expected, htmlstring)
    
    def test_parent_three_children(self):
        leafnode1 = LeafNode("This is a paragraph.")
        leafnode2 = LeafNode("Some italics.")
        leafnode3 = LeafNode("Title.")

        parent = ParentNode("b", [leafnode1, leafnode2, leafnode3])

        self.assertEqual(parent.tag, "b")
        self.assertEqual(parent.children, [leafnode1, leafnode2, leafnode3])
        self.assertEqual(parent.props, None)

        htmlstring = parent.to_html()
        expected = "<b>This is a paragraph.Some italics.Title.</b>"
        self.assertEqual(expected, htmlstring)

    def test_grandparenting(self):
        leafnode = LeafNode("This is a paragraph.")
        parent = ParentNode("b",[leafnode])
        grandparent = ParentNode("u",[parent])

        self.assertEqual(grandparent.tag, "u")
        
        htmlstring = grandparent.to_html()
        expected = "<u><b>This is a paragraph.</b></u>"
        self.assertEqual(htmlstring, expected)