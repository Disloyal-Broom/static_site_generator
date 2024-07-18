import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p","this is a paragraph text","test","test2")
        expected_result = 'HTMLNode(p,this is a paragraph text,test,test2)'
        self.assertEqual(node.__repr__(),expected_result)
        
    def test_props_to_html(self):
        node = HTMLNode("h1", "Some Text", "href", {"href": "https://www.google.com","target": "_blank"})
        expected_result = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),expected_result)

    def test_eq(self):
        node = HTMLNode("h1", "Some Text", "href", {"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode("h1", "Some Text", "href", {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node,node2)
        
    def test_not_eq(self):
        node = HTMLNode("h1", "Some Text", "href", {"href": "https://www.google.com","target": "_blank"})
        node2 = HTMLNode("p","this is a paragraph text","test","test2")
        self.assertIsNot(node,node2)

if __name__ == "__main__":
    unittest.main()
