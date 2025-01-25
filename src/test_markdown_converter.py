import unittest

from markdown_converter import markdown_to_blocks, block_to_block_type

class testmarkdowntoblocks(unittest.TestCase):
    def test_markdowntoblocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside it."
        blocks = markdown_to_blocks(text)
        #print(blocks)
        self.assertEqual(blocks[0],"# This is a heading")
        self.assertEqual(blocks[1],"This is a paragraph of text. It has some **bold** and *italic* words inside it.")

    def test_markdowntoblocks2(self):
        text = "# Heading\n\nParagraph\n\n* List item"
        blocks = markdown_to_blocks(text)
        #print(blocks)
        self.assertEqual(len(blocks),3)
        self.assertEqual(blocks[0],"# Heading")
        self.assertEqual(blocks[1],"Paragraph")
        self.assertEqual(blocks[2],"* List item")

    def test_markdowntoblocks_with_spaces(self):
        text = "# This is a heading   \n\n   This is a paragraph of text. It has some **bold** and *italic* words inside it.  "
        blocks = markdown_to_blocks(text)
        #print(blocks)
        self.assertEqual(blocks[0],"# This is a heading")
        self.assertEqual(blocks[1],"This is a paragraph of text. It has some **bold** and *italic* words inside it.")
    
    def test_block_convert_heading(self):
        text = "# This is a heading"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype, "heading")
    
    def test_block_convert_heading_leading_space(self):
        text = "#This is a heading without a leading space"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype, "paragraph")
    
    def test_block_convert_code(self):
        text = "```Some block code```"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype, "code")
    
    def test_block_convert_code_no_opener(self):
        text = "Some block code```"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype, "paragraph")
    
    def test_block_convert_code_no_closer(self):
        text = "```Some block code"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype, "paragraph")
    
    def test_block_convert_quote_single(self):
        text = ">A quote"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"quote")

    def test_block_convert_quote_multiple(self):
        text = ">A quote\n>With\n>Multiple lines"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"quote")
    
    def test_block_convert_quote_mult_incomplete(self):
        text = ">A quote\n>With\nMultiple lines but not all with >"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"paragraph")
    
    def test_block_convert_ulist_single(self):
        text = "* Single list"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"unordered_list")

    def test_block_convert_ulist_multiple(self):
        text = "* An item\n* Another item\n* A third"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"unordered_list")
    
    def test_block_convert_ulist_multiple_incomplete(self):
        text = "* An item\n* Another item\nA third but no opener"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"paragraph")
    
    def test_block_convert_olist_single(self):
        text = "1. Single list"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"ordered_list")

    def test_block_convert_olist_multiple(self):
        text = "1. An item\n2. Another item\n3. A third"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"ordered_list")
    
    def test_block_convert_olist_multiple_incomplete(self):
        text = "1. An item\n2. Another item\nA third but no opener"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"paragraph")
    
    def test_block_convert_olist_multiple_outoforder(self):
        text = "1. An item\n2. Another item\n4.A third but no opener"
        blocktype = block_to_block_type(text)
        self.assertEqual(blocktype,"paragraph")