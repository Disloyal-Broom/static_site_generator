import unittest
from textnode import *
from split_nodes_link import * 

class TestSplitNodeslink(unittest.TestCase):
    def test_single_link(self):
        node = split_nodes_link([TextNode(
    "This is text with an link [to boot dev](https://www.boot.dev) some text",
    'text')])
        
        expected_results = [TextNode('This is text with an link ','text'),
                            TextNode('to boot dev','link','https://www.boot.dev'),
                            TextNode(' some text', 'text')
                            ]
        self.assertEqual(node,expected_results)

    def test_double_link(self):
        node = split_nodes_link([TextNode('links are [pretty cool](www.google.com) especially [two](www.ff.com) some text','text')])
        expected_results = [TextNode('links are ','text'),
                            TextNode('pretty cool','link','www.google.com'),
                            TextNode(' especially ','text'),
                            TextNode('two','link','www.ff.com'),
                            TextNode(' some text','text')]
        self.assertEqual(node,expected_results)

    def test_two_link_nodes(self):
        node = split_nodes_link([TextNode('some [link](www.link.com)','text'),
                                  TextNode('another [link](www.okaybois.com) is fine too','text')])
        expected_results = [
            TextNode('some ','text'),
            TextNode('link','link','www.link.com'),
            TextNode('another ','text'),
            TextNode('link','link','www.okaybois.com'),
            TextNode(' is fine too','text')
        ]
        self.assertEqual(node,expected_results)

    def test_no_link(self):
        node = split_nodes_link([TextNode('this node has no link','text')])
        expected_results = [TextNode('this node has no link','text')]
        self.assertEqual(node,expected_results)

    def test_one_link_one_no_link(self):
        node = split_nodes_link([TextNode('There is [an link](https://link.com) in here.','text'),
                                  TextNode('but none in here.','text')])
        expected_results = [
            TextNode('There is ','text'),
            TextNode('an link','link','https://link.com'),
            TextNode(' in here.','text'),
            TextNode('but none in here.','text')
        ]
        self.assertEqual(node,expected_results)

    def test_link_at_start(self):
        node = split_nodes_link([TextNode('[an link](https://link.com) at the start','text')])
        expected_results = [TextNode('an link','link','https://link.com'),
                            TextNode(' at the start','text')]
        self.assertEqual(node,expected_results)

    def test_link_at_end(self):
        node = split_nodes_link([TextNode('here is an ending [link](www.link.com)','text')])
        expected_results = [
            TextNode('here is an ending ', 'text'),
            TextNode('link','link','www.link.com')
        ]
        self.assertEqual(node,expected_results)

    def test_no_link_one_link(self):
        node = split_nodes_link([
            TextNode('there is no link here','text'),
            TextNode('but [there is one here](www.link.com)','text')
        ])
        expected_results = [
            TextNode('there is no link here','text'),
            TextNode('but ','text'),
            TextNode('there is one here','link','www.link.com')
        ]
        self.assertEqual(node, expected_results)

if __name__ == "__main__":
    unittest.main()