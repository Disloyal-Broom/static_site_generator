import unittest
from text_to_textnodes import *
from textnode import *

class TestTextToTextNodes(unittest.TestCase):
    def test_basic_text(self):
        test_case = text_to_textnodes("this is a test text")
        expected_results = [
            TextNode('this is a test text','text')
        ]
        self.assertEqual(test_case,expected_results)
        
    def test_bold_ast(self):
        test_case = text_to_textnodes("this could **be bold**?")
        expected_results = [
            TextNode('this could ','text'),
            TextNode('be bold','bold'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_bold_underline(self):
        test_case = text_to_textnodes("this could __be bold__?")
        expected_results = [
            TextNode('this could ','text'),
            TextNode('be bold','bold'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_italics_ast(self):
        test_case = text_to_textnodes("this could *be italized*?")
        expected_results = [
            TextNode('this could ','text'),
            TextNode('be italized','italics'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_italics_underline(self):
        test_case = text_to_textnodes("this could _be italized_?")
        expected_results = [
            TextNode('this could ','text'),
            TextNode('be italized','italics'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_bold_italics_ast(self):
        test_case = text_to_textnodes("this could be ***bold and italized***?")
        expected_results = [
            TextNode('this could be ','text'),
            TextNode('bold and italized','bold&italics'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_bold_italics_underline(self):
        test_case = text_to_textnodes("this could be ___bold and italized___?")
        expected_results = [
            TextNode('this could be ','text'),
            TextNode('bold and italized','bold&italics'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_code(self):
        test_case = text_to_textnodes("this could be 'code'?")
        expected_results = [
            TextNode('this could be ','text'),
            TextNode('code','code'),
            TextNode('?','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_bold_link(self):
        test_case = text_to_textnodes("this could be **bold** and this could be [a rickroll!](https://rickroll.com)!")
        expected_results = [
            TextNode('this could be ','text'),
            TextNode('bold','bold'),
            TextNode(' and this could be ','text'),
            TextNode('a rickroll!','link','https://rickroll.com'),
            TextNode('!','text')
        ]
        self.assertEqual(test_case,expected_results)

    def test_two_links(self):
        text_case = text_to_textnodes("this [is a link](https://google.com) very cool [huh](https://notreally.no).")
        expected_results = [
            TextNode('this ','text'),
            TextNode('is a link','link','https://google.com'),
            TextNode(' very cool ','text'),
            TextNode('huh','link','https://notreally.no'),
            TextNode('.','text')
        ]
        self.assertEqual(text_case,expected_results)
        
    def test_image(self):
        test_case = text_to_textnodes("![i like](google.com) so much")
        expected_results = [
            TextNode('i like','image','google.com'),
            TextNode(' so much','text')
        ]
        self.assertEqual(test_case, expected_results)
        
    def test_two_images(self):
        test_case = text_to_textnodes('i ![like](friend.com) and ![amung](.us) is cool too')
        expected_results = [
            TextNode('i ','text'),
            TextNode('like','image','friend.com'),
            TextNode(' and ','text'),
            TextNode('amung','image','.us'),
            TextNode(' is cool too','text')
        ]
        self.assertEqual(test_case,expected_results)
    
    def test_image_in_front(self):
        test_case = text_to_textnodes('![image](image.com) up front')
        expected_results = [
            TextNode('image','image','image.com'),
            TextNode(' up front','text', None)
        ]
        self.assertEqual(test_case,expected_results)
        
    def test_image_in_back(self):
        test_case = text_to_textnodes('in back ![image](image.com)')
        expected_results = [
            TextNode('in back ','text',None),
            TextNode('image','image','image.com')
        ]
        self.assertEqual(test_case,expected_results)
       
    def test_image_link(self):
        test_case = text_to_textnodes('here is an ![image](image.com), and a [link](link.com).')
        expected_results = [
            TextNode('here is an ','text'),
            TextNode('image','image','image.com'),
            TextNode(', and a ','text'),
            TextNode('link','link','link.com'),
            TextNode('.','text')
        ]
        self.assertEqual(test_case,expected_results)
        
    def test_link_image(self):
        test_case = text_to_textnodes('here is an [link](link.com), and a ![image](image.com).')
        expected_results = [
            TextNode('here is an ','text'),
            TextNode('link','link','link.com'),
            TextNode(', and a ','text'),
            TextNode('image','image','image.com'),
            TextNode('.','text')
        ]
        self.assertEqual(test_case,expected_results)
    
    def test_link_front(self):
        test_case = text_to_textnodes('[link](link.com) test')
        expected_results = [
            TextNode('link','link','link.com'),
            TextNode(' test','text', None)
        ]
        self.assertEqual(test_case,expected_results)
        
    def test_link_back(self):
        test_case = text_to_textnodes('the [link](link.com)')
        expected_results = [
            TextNode('the ','text', None),
            TextNode('link','link','link.com')
        ]
        self.assertEqual(test_case,expected_results)
    
    def test_5_different_types(self):
        test_case = text_to_textnodes('Here are **bold words** followed by *italized words* with an ![image](image.com) and a [link](link.com)')
        expected_results = [
            TextNode('Here are ','text'),
            TextNode('bold words','bold'),
            TextNode(' followed by ','text'),
            TextNode('italized words','italics'),
            TextNode(' with an ','text'),
            TextNode('image','image','image.com'),
            TextNode(' and a ','text'),
            TextNode('link','link','link.com')
        ]
        self.assertEqual(test_case,expected_results)
        
if __name__ == "__main__":
    unittest.main()