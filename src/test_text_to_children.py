import unittest
from htmlnode import *
from text_to_children import *

class TestTextToChildren(unittest.TestCase):
    def test_h1(self):
        result = text_to_children('# h1 heading')
        expected_result = HTMLNode('h1','# h1 heading', None, None)
        self.assertEqual(result,expected_result)

    def test_h2(self):
        result = text_to_children('## h2 heading')
        expected_result = HTMLNode('h2','## h2 heading', None, None)
        self.assertEqual(result,expected_result)

    def test_h3(self):
        result = text_to_children('### h3 heading')
        expected_result = HTMLNode('h3','### h3 heading', None, None)
        self.assertEqual(result,expected_result)

    def test_h4(self):
        result = text_to_children('#### h4 heading')
        expected_result = HTMLNode('h4','#### h4 heading', None, None)
        self.assertEqual(result,expected_result)

    def test_h5(self):
        result = text_to_children('##### h5 heading')
        expected_result = HTMLNode('h5','##### h5 heading', None, None)
        self.assertEqual(result,expected_result)

    def test_h6(self):
        result = text_to_children('###### h6 heading')
        expected_result = HTMLNode('h6','###### h6 heading', None, None)
        self.assertEqual(result,expected_result)

    def test_blockquote(self):
        result = text_to_children('> quote')
        expected_result = HTMLNode('blockquote', '> quote', None, None)
        self.assertEqual(result, expected_result)

    def test_unordered_list(self):
        result = text_to_children('* this\n* is\n* a list')
        expected_result = HTMLNode('ul', '* this\n* is\n* a list', None, None)
        self.assertEqual(result, expected_result)

    def test_ordered_list(self):
        result = text_to_children('1. this\n2. is\n3. a list')
        expected_result = HTMLNode('ol', '1. this\n2. is\n3. a list', None, None)
        self.assertEqual(result, expected_result)

    def test_code(self):
        result = text_to_children('``` code ```')
        expected_result = HTMLNode('code', '``` code ```', None, None)
        self.assertEqual(result, expected_result)
        
    def test_paragraph(self):
        result = text_to_children('this is a paragraph')
        expected_result = HTMLNode('p', 'this is a paragraph', None, None)
        self.assertEqual(result, expected_result)

    def test_unknown(self):
        result = text_to_children('$HYFVNDEKWO()')
        expected_result = HTMLNode('p', '$HYFVNDEKWO()', None, None)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()