import unittest
from split_node_delimiter import *

class Test_Split_Node_Delimiter(unittest.TestCase):
    def test_bold_ast_ast(self):
        nodes = split_nodes_delimiter([TextNode('This **word** is bold.','text'), TextNode('**These words** are bold','text')], '**','text')
        
        expected_results = [TextNode('This ','text'),
                            TextNode('word','bold'),
                            TextNode(' is bold.','text'),
                            TextNode('These words','bold'),
                            TextNode(' are bold','text')]
                            
        self.assertEqual(nodes, expected_results)
    
    def test_bold_underline_underline(self):
        nodes = split_nodes_delimiter([TextNode('This __word__ is bold.','text')],'__','text')
        expected_results = [TextNode('This ','text'),
                            TextNode('word','bold'),
                            TextNode(' is bold.','text')] 
        self.assertEqual(nodes,expected_results)
        
    def test_italics(self):
        nodes = split_nodes_delimiter([TextNode('This *word* should be italizied','text')],'*','text')
        expected_result = [TextNode('This ','text'),
                           TextNode('word','italics'),
                           TextNode(' should be italizied','text')]
        self.assertEqual(nodes,expected_result)

    def test_italics_underline(self):
        nodes = split_nodes_delimiter([TextNode('This _word_ should be italizied','text')],'_','text')
        expected_result = [TextNode('This ','text'),
                    TextNode('word','italics'),
                    TextNode(' should be italizied','text')]
        self.assertEqual(nodes,expected_result)

    def test_bold_italics_ast(self):
        nodes = split_nodes_delimiter([TextNode('This ***should be bold*** and italized','text')],'***', 'text')
        expected_result = [TextNode('This ','text'),
                           TextNode('should be bold','bold&italics'),
                           TextNode(' and italized', 'text')]
        self.assertEqual(nodes, expected_result)

    def test_bold_italics_underline(self):
        nodes = split_nodes_delimiter([TextNode('This ___should be bold___ and italized','text')],'___','text')
        expected_result = [TextNode('This ','text'),
                           TextNode('should be bold','bold&italics'),
                           TextNode(' and italized', 'text')]
        self.assertEqual(nodes,expected_result)

    def test_code(self):
        nodes = split_nodes_delimiter([TextNode("This is `code:` woohoo",'text')],"`",'text')
        expected_result = [TextNode('This is ', 'text'),
                           TextNode("code:" ,'code'),
                           TextNode(" woohoo",'text')]
        self.assertEqual(nodes,expected_result)

    def test_delimiter_at_start(self):
        nodes = split_nodes_delimiter([TextNode("**Bold** of you to say that.",'text')],'**','text')
        expected_result = [TextNode('Bold', 'bold'),
                           TextNode(' of you to say that.','text')]
        self.assertEqual(nodes,expected_result)

    def test_delimiter_at_end(self):
        nodes = split_nodes_delimiter([TextNode("Bold of you to say **that.**",'text')],'**','text')
        expected_results = [TextNode('Bold of you to say ','text'),
                            TextNode('that.','bold')]
        self.assertEqual(nodes,expected_results)

    def test_no_delimiter(self):
        nodes = split_nodes_delimiter([TextNode('no delimiter to be found','text')],'','text')
        expected_results = [TextNode('no delimiter to be found','text')]
        self.assertEqual(nodes, expected_results)
    
    def test_empty(self):
        nodes = split_nodes_delimiter([],'*','text')
        expected_results = []
        self.assertEqual(nodes,expected_results)
        
if __name__ == "__main__":
    unittest.main()