import unittest
from markdown_to_leaf_node import *
from leafnode import *

class TestMarkdownToLeafnode(unittest.TestCase):
    def test_headers1_6(self):
        leaf_nodes = markdown_to_leaf_node("""# heading 1
## heading 2

### heading 3
#### heading 4

##### heading 5
###### heading 6""")
        expected_results = [
            LeafNode('h1','# heading 1'),
            LeafNode('h2','## heading 2'),
            LeafNode('h3','### heading 3'),
            LeafNode('h4','#### heading 4'),
            LeafNode('h5','##### heading 5'),
            LeafNode('h6','###### heading 6')
        ]
        self.assertEqual(leaf_nodes, expected_results)

    def test_quotes(self):
        leafnodes = markdown_to_leaf_node("""> this
> is
> a
> quote""")
        expected_results = [
            LeafNode('blockquote','> this'),
            LeafNode('blockquote','> is'),
            LeafNode('blockquote','> a'),
            LeafNode('blockquote','> quote')
        ]
        self.assertEqual(leafnodes,expected_results)
        
    def test_headers_and_quotes(self):
        leafnodes = markdown_to_leaf_node("""# Hello World
> the world
> says hello
> -
> someone

## Hello world 2


> quote 2""")
        expected_results = [
            LeafNode('h1','# Hello World'),
            LeafNode('blockquote','> the world'),
            LeafNode('blockquote','> says hello'),
            LeafNode('blockquote','> -'),
            LeafNode('blockquote','> someone'),
            LeafNode('h2','## Hello world 2'),
            LeafNode('blockquote', '> quote 2')
        ]
        self.assertEqual(leafnodes,expected_results)
        
    def test_heading_quote_bold(self):
        leafnode = markdown_to_leaf_node("""## header 2
this is *italics* text and **bold** text
> quoting something""")
        expected_results = [
            LeafNode('h2','## header 2'),
            LeafNode('p', 'this is '),
            LeafNode('em', 'italics'),
            LeafNode('p',' text and '),
            LeafNode('strong','bold'),
            LeafNode('p',' text'),
            LeafNode('blockquote','> quoting something')
        ]
        self.assertEqual(leafnode,expected_results)
        
if __name__ == '__main__':
    unittest.main()