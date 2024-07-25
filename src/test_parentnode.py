import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p", None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_result = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(),expected_result)
    
    def test_to_html_empty_child(self):
        node = ParentNode('p', None, None)
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "Error: Children is empty.")

    def test_to_html_empty_tag(self):
        node = ParentNode(None, None,
                          [LeafNode(None,"some text"),
                           LeafNode(None,"other text")
                           ])
        with self.assertRaises(ValueError) as context:
            node.to_html()
            
        self.assertEqual(str(context.exception), "Error: Tag is empty.")
    
    def test_to_html_nested_parents(self):
        node = ParentNode(
            "p", None,
            [
                ParentNode("p", None, [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                    ]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_result = '<p><p>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_result)
    
    def test_to_html_double_nested_parents(self):
        node = ParentNode(
            "p", None,
            [
                ParentNode("p", None, [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    ParentNode("p", None, [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        ])
                    ]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_result = '<p><p>Normal text<i>italic text</i><p>Normal text<i>italic text</i></p></p>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_result)
    
    def test_to_html_h1(self):
        node = ParentNode('h1', None, [
            LeafNode('p','heyo'),
            LeafNode('a','some text',{
                'href':'www.google.com',
                'target':'__blank'})
        ])
        expected_results = '<h1><p>heyo</p>href="www.google.com" target="__blank"</h1>'
        self.assertEqual(node.to_html(),expected_results)
    
    def test_to_html_empty_child_list(self):
        node = ParentNode('p', None, [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
            
        self.assertEqual(str(context.exception),"Error: Children is empty.")
    
    def test_to_html_lists(self):
        node = ParentNode('div', None, [
            LeafNode('p', 'Paragraph text'),
            ParentNode('ul', None, [
                LeafNode('li', 'List item 1'),
                LeafNode('li', 'List item 2')
            ])
        ])
        
        expected_html = '<div><p>Paragraph text</p><ul><li>List item 1</li><li>List item 2</li></ul></div>'
        self.assertEqual(node.to_html(), expected_html)
    
    def test_repr(self):
        node = ParentNode(
            "p", None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_result = f'ParentNode(p, None, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)'
        self.assertEqual(node.__repr__(),expected_result)
        
if __name__ == "__main__":
    unittest.main()