import unittest
from markdown_to_blocks import * 

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_functionality(self):
        text = markdown_to_blocks("""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
""")
        expected_results = ['# This is a heading',
                            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                            '* This is the first list item in a list block',
                            '* This is a list item',
                            '* This is another list item']
        self.assertEqual(text,expected_results)

    def test_different_md(self):
        text = markdown_to_blocks("""# This is heading1
                                  
## This is heading2
### This is heading3
                                  
Paragraphs for good measure
                                  
* List Item 1
* List Item 2
                                  



Lotsa space in between.
""")
        expected_results = ['# This is heading1',
                            '## This is heading2',
                            '### This is heading3',
                            'Paragraphs for good measure',
                            '* List Item 1',
                            '* List Item 2',
                            'Lotsa space in between.']
        self.assertEqual(expected_results,text)

    def test_space_start(self):
        text = markdown_to_blocks("""
                                  
How do you do?
## testing text
                                  
                                  
                                  
                                  
> 1
> 2
> 3
""" )
        expected_results = ['How do you do?',
                            '## testing text',
                            '> 1',
                            '> 2',
                            '> 3']
        self.assertEqual(text,expected_results)

    def test_space_end(self):
        text = markdown_to_blocks(""" text is at the start
blah 
                                    
blah 

                                    
                                    
                                    
                                    
                                    """)
        expected_results = [' text is at the start',
                            'blah ',
                            'blah ']
        self.assertEqual(text,expected_results)

    def test_long_form(self):
        text = markdown_to_blocks("""
## Typographic replacements

Enable typographer option to see result.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,,  -- ---

"Smartypants, double quotes" and 'single quotes'


## Emphasis

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~


## Blockquotes


> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.""")
        expected_results = [
            '## Typographic replacements',
            'Enable typographer option to see result.',
            '(c) (C) (r) (R) (tm) (TM) (p) (P) +-',
            'test.. test... test..... test?..... test!....',
            '!!!!!! ???? ,,  -- ---',
            '"Smartypants, double quotes" and \'single quotes\'',
            '## Emphasis',
            '**This is bold text**',
            '__This is bold text__',
            '*This is italic text*',
            '_This is italic text_',
            '~~Strikethrough~~',
            '## Blockquotes',
            '> Blockquotes can also be nested...',
            '>> ...by using additional greater-than signs right next to each other...',
            '> > > ...or with spaces between arrows.'
        ]
        self.assertEqual(text,expected_results)

if __name__ == "__main__":
    unittest.main()