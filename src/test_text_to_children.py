import unittest
from htmlnode import *
from text_to_children import *

class TestTextToChildren(unittest.TestCase):
    def test_h1(self):
        result = text_to_children('# h1 heading')
        expected_result = [
            TextNode('# h1 heading','h1', None)
        ]
        self.assertEqual(result,expected_result)

    def test_h2(self):
        result = text_to_children('## h2 heading')
        expected_result = [
            TextNode('## h2 heading','h2', None)
        ]
        self.assertEqual(result,expected_result)

    def test_h3(self):
        result = text_to_children('### h3 heading')
        expected_result = [
            TextNode('### h3 heading','h3', None)
        ]
        self.assertEqual(result,expected_result)

    def test_h4(self):
        result = text_to_children('#### h4 heading')
        expected_result = [
            TextNode('#### h4 heading','h4', None)
        ]
        self.assertEqual(result,expected_result)

    def test_h5(self):
        result = text_to_children('##### h5 heading')
        expected_result = [
            TextNode('##### h5 heading','h5', None)
        ]
        self.assertEqual(result,expected_result)

    def test_h6(self):
        result = text_to_children('###### h6 heading')
        expected_result = [
            TextNode('###### h6 heading','h6', None)
        ]
        self.assertEqual(result,expected_result)

    def test_blockquote(self):
        result = text_to_children('> quote')
        expected_result = [
            TextNode('> quote', 'blockquote', None)
        ]
        self.assertEqual(result, expected_result)

    def test_unordered_list(self):
        result = text_to_children('* this\n* is\n* a list')
        expected_result = [
            TextNode('* this', 'ul', None),
            TextNode('* is', 'ul', None),
            TextNode('* a list','ul',None)
        ]
        self.assertEqual(result, expected_result)

    def test_ordered_list(self):
        result = text_to_children('1. this\n2. is\n3. a list')
        expected_result = [
            TextNode('1. this', 'ol', None),
            TextNode('2. is','ol',None),
            TextNode('3. a list','ol',None)
        ]
        self.assertEqual(result, expected_result)

    def test_code(self):
        result = text_to_children('``` code ```')
        expected_result = [
            TextNode('``` code ```', 'code', None)
        ]
        self.assertEqual(result, expected_result)
        
    def test_paragraph(self):
        result = text_to_children('this is a paragraph')
        expected_result = [
            TextNode('this is a paragraph', 'text', None)
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()