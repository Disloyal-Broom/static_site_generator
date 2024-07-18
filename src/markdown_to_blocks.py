
delimiter_to_text_type = {
    '#####':'heading5',
    '####':'heading4',
    '###':'heading3',
    '##':'heading2',
    '#':'heading1', 
    '\n':'break',
    '>':'blockquote',
    #TODO: add order list functionality r'number':'list'
    '-':'unorderedlist',
    '+':'unorderedlist',
    '* ':'unorderedlist',
    '\t*':'unorderedlist',
}
def markdown_to_blocks(md_text):
    block = md_text.split('\n')
    
    for chunk in block:
        if chunk == '':
            block.remove(chunk)
            
    return block


text = r"""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

print(markdown_to_blocks(text))

#example 
'''
input:
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

output: 
[
    "# This is a heading",
    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
    "* This is the first list item in a list block
    * This is a list item
    * This is another list item",
]
'''