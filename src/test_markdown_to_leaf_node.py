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

if __name__ == '__main__':
    unittest.main()