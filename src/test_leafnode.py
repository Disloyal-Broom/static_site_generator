import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode('p','some text')
        expected_result = f'LeafNode({node.tag}, {node.value}, {node.props})'
        self.assertEqual(node.__repr__(),expected_result)
    
    def test_to_html_p(self):
        node = LeafNode('p','some text')
        expected_result = '<p>some text</p>'
        self.assertEqual(node.to_html(),expected_result)
        
    def test_to_html_a(self):
        node = LeafNode('a', 'some text',{"href": "https://www.google.com","target": "_blank"})
        expected_result = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),expected_result)
    
    def test_to_html_plain(self):
        node = LeafNode(None,'some text')
        expected_result = 'some text'
        self.assertEqual(node.to_html(),expected_result)

    def test_to_html_i(self):
        node = LeafNode('i','some text')
        expected_result = '<i>some text</i>'
        self.assertEqual(node.to_html(),expected_result)
        
    def test_to_html_b(self):
        node = LeafNode('b','some text')
        expected_result = '<b>some text</b>'
        self.assertEqual(node.to_html(),expected_result)
        
        
if __name__ == "__main__":
    unittest.main()
