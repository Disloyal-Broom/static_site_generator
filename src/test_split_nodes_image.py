import unittest
from textnode import *
from split_nodes_image import * 

class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = split_nodes_image([TextNode(
    "This is text with an image ![to boot dev](https://www.boot.dev) some text",
    'text')])
        
        expected_results = [TextNode('This is text with an image ','text'),
                            TextNode('to boot dev','image','https://www.boot.dev'),
                            TextNode(' some text', 'text')
                            ]
        self.assertEqual(node,expected_results)

    def test_double_image(self):
        node = split_nodes_image([TextNode('images are ![pretty cool](www.google.com) especially ![two](www.ff.com) some text','text')])
        expected_results = [TextNode('images are ','text'),
                            TextNode('pretty cool','image','www.google.com'),
                            TextNode(' especially ','text'),
                            TextNode('two','image','www.ff.com'),
                            TextNode(' some text','text')]
        self.assertEqual(node,expected_results)

    def test_two_image_nodes(self):
        node = split_nodes_image([TextNode('some ![image](www.image.com)','text'),
                                  TextNode('another ![image](www.okaybois.com) is fine too','text')])
        expected_results = [
            TextNode('some ','text'),
            TextNode('image','image','www.image.com'),
            TextNode('another ','text'),
            TextNode('image','image','www.okaybois.com'),
            TextNode(' is fine too','text')
        ]
        self.assertEqual(node,expected_results)

    def test_no_image(self):
        node = split_nodes_image([TextNode('this node has no image','text')])
        expected_results = [TextNode('this node has no image','text')]
        self.assertEqual(node,expected_results)

    def test_one_image_one_no_image(self):
        node = split_nodes_image([TextNode('There is ![an image](https://image.com) in here.','text'),
                                  TextNode('but none in here.','text')])
        expected_results = [
            TextNode('There is ','text'),
            TextNode('an image','image','https://image.com'),
            TextNode(' in here.','text'),
            TextNode('but none in here.','text')
        ]
        self.assertEqual(node,expected_results)

    def test_image_at_start(self):
        node = split_nodes_image([TextNode('![an image](https://image.com) at the start','text')])
        expected_results = [TextNode('an image','image','https://image.com'),
                            TextNode(' at the start','text')]
        self.assertEqual(node,expected_results)

    def test_image_at_end(self):
        node = split_nodes_image([TextNode('here is an ending ![image](www.image.com)','text')])
        expected_results = [
            TextNode('here is an ending ', 'text'),
            TextNode('image','image','www.image.com')
        ]
        self.assertEqual(node,expected_results)

    def test_no_image_one_image(self):
        node = split_nodes_image([
            TextNode('there is no image here','text'),
            TextNode('but ![there is one here](www.image.com)','text')
        ])
        expected_results = [
            TextNode('there is no image here','text'),
            TextNode('but ','text'),
            TextNode('there is one here','image','www.image.com')
        ]
        self.assertEqual(node, expected_results)

if __name__ == "__main__":
    unittest.main()