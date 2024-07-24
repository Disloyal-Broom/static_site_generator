import unittest
from leafnode_to_parentnode import *

class TestLeafnodeToParentnode(unittest.TestCase):
    def test_p_strong(self):
        parent_nodes = leafnode_to_parentnode([
            LeafNode('p','test text '),
            LeafNode('strong', 'that is bold '),
            LeafNode('p','but this is not')
        ])
        expected_result = [
            ParentNode('p','test text ', [
                LeafNode('strong','that is bold '),
                LeafNode('p','but his is not')
            ])
        ]
        self.assertEqual(parent_nodes,expected_result)
        
    def test_p_strong_italics(self):
        parent_nodes = leafnode_to_parentnode([
            LeafNode('p','test text '),
            LeafNode('strong', 'that is bold '),
            LeafNode('p','but this is not '),
            LeafNode('em','italized'),
            LeafNode('p',' but again this isnt')
        ])
        expected_result = [
            ParentNode('p','test text ', [
                LeafNode('strong','that is bold '),
                ParentNode('p','but his is not ',[
                    LeafNode('em','italized'),
                    LeafNode('p',' but again this isnt')])
            ])
        ]
        self.assertEqual(parent_nodes, expected_result)

        

if __name__ == "__main__":
    unittest.main()