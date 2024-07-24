import unittest
from textnode_to_htmlnode import *
from textnode import *

class Test_TextNode_To_HTMLNode(unittest.TestCase):
    def test_text(self):
        textnode = TextNode("Some Text","text")
        node = text_node_to_html_node(textnode)
        expected_results = LeafNode('p','Some Text')
        self.assertEqual(node, expected_results)
        
    def test_bold(self):
        textnode = TextNode("Some Text",'bold')
        node = text_node_to_html_node(textnode)
        expected_results = LeafNode('strong','Some Text')
        self.assertEqual(node,expected_results)
        
    def test_italic(self):
        textnode = TextNode('some text','italic')
        node = text_node_to_html_node(textnode)
        expected_results = LeafNode('em','some text')
        self.assertEqual(node,expected_results)
        
    def test_code(self):
        textnode = TextNode('some text','code')
        node = text_node_to_html_node(textnode)
        expected_results = LeafNode('code','some text')
        self.assertEqual(node,expected_results)
        
    def test_link(self):
        textnode = TextNode('some text','link','www.google.com')
        node = text_node_to_html_node(textnode)
        expected_results = LeafNode('link','some text',{'href':'www.google.com'})
        self.assertEqual(node,expected_results)
        
    def test_image(self):
        textnode = TextNode('some text','image','www.google.com')
        node = text_node_to_html_node(textnode)
        expected_results = LeafNode('image','',{'src':'www.google.com', 'alt':'some text'})
        self.assertEqual(node, expected_results)

    def test_not_found(self):
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(TextNode('some text','asdf'))
            
        self.assertEqual(str(context.exception),'TextNode_Type: asdf not found.')
        
if __name__ == "__main__":
    unittest.main()
