import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Some Text","Underlined")
        expected_print = "TextNode(Some Text, Underlined, None)"
        self.assertEqual(node.__repr__(),expected_print)
        
    def test_not_eq_url(self):
        node = TextNode("Some Text", "Bold", "www.me.com")
        node2 = TextNode("Some Text","Bold")
        self.assertIsNot(node,node2)

    def test_not_eq_type(self):
        node = TextNode("Some Text", "Underlined")
        node2 = TextNode("Some Text","Bold")
        self.assertIsNot(node,node2)
        
    def test_not_eq_string(self):
        node = TextNode("Dif Text", "Bold")
        node2 = TextNode("Some Text","Bold")
        self.assertIsNot(node,node2)
        
if __name__ == "__main__":
    unittest.main()
