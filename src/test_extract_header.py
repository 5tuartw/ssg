import unittest
from extract_header import *

class testheaderextract(unittest.TestCase):

    def test_find_header_first_line(self):
        file = "headertest1.md" # header on first line
        header = extract_title(file)
        self.assertEqual(header, "The Header")

        file = "headertest2.md" # header not on first line
        header = extract_title(file)
        self.assertEqual(header, "The real header")        

        file = "headertest3.md" # no header
        with self.assertRaises(Exception) as context:
            header = extract_title(file)
        self.assertEqual(str(context.exception), f"No h1 header found in {file}")

        file = "headertest4.md" # header but with special characters
        header = extract_title(file)
        self.assertEqual(header, "<> £ `The Header")