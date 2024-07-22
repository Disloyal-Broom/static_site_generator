import unittest
from block_to_block_type import *

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block_type = block_to_block_type('# block')
        expected_result = "heading"
        self.assertEqual(block_type,expected_result)

    def test_to_many_heading(self):
        block_type = block_to_block_type('################## heading?')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
    def test_no_heading(self):
        block_type = block_to_block_type('some text')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)

    def test_heading6(self):
        block_type = block_to_block_type('###### heading6')
        expected_result = 'heading'
        self.assertEqual(block_type,expected_result)

    def test_heading5(self):
        block_type = block_to_block_type('##### heading5')
        expected_result = 'heading'
        self.assertEqual(block_type,expected_result)

    def test_heading4(self):
        block_type = block_to_block_type('#### heading4')
        expected_result = 'heading'
        self.assertEqual(block_type,expected_result)
        
    def test_heading3(self):
        block_type = block_to_block_type('### heading3')
        expected_result = 'heading'
        self.assertEqual(block_type,expected_result)
        
    def test_heading2(self):
        block_type = block_to_block_type('## heading2')
        expected_result = 'heading'
        self.assertEqual(block_type,expected_result)
        
    def test_code(self):
        block_type = block_to_block_type('``` this is code```')
        expected_result = 'code'
        self.assertEqual(block_type, expected_result)
        
    def test_code_middle(self):
        block_type = block_to_block_type('this isnt code but ```this is ```')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
    def test_quote(self):
        block_type = block_to_block_type('> test')
        expected_result = 'quote'
        self.assertEqual(block_type,expected_result)
        
    def test_newline_quote(self):
        block_type = block_to_block_type('> test\n> quote')
        expected_result = 'quote'
        self.assertEqual(block_type,expected_result)
        
    def test_newline_not_quote(self):
        block_type = block_to_block_type('> quote\nnot a quote')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
    def test_not_quote(self):
        block_type = block_to_block_type('asdf > quote?')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
    def test_unordered_list_ask(self):
        block_type = block_to_block_type('* word\n* word')
        expected_result = 'unorderedlist'
        self.assertEqual(block_type,expected_result)
        
    def test_unordered_list_dash(self):
        block_type = block_to_block_type('- word\n- word')
        expected_result = 'unorderedlist'
        self.assertEqual(block_type,expected_result)
        
    def test_not_unordered_list_ask(self):
        block_type = block_to_block_type('* word\nsome text')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
    def test_not_unordered_list_dash(self):
        block_type = block_to_block_type('- word\nsome text')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
    def test_ordered_list(self):
        block_type = block_to_block_type('1. text\n2. text \n3. text')
        expected_result = 'orderedlist'
        self.assertEqual(block_type,expected_result)
        
    def test_not_ordered_list(self):
        block_type = block_to_block_type('1. text\n3. text\n2. text \n3. text')
        expected_result = 'paragraph'
        self.assertEqual(block_type,expected_result)
        
if __name__ == "__main__":
    unittest.main()