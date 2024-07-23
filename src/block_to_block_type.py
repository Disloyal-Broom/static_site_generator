import re

def block_to_block_type(block):
    heading_pattern = r'^\#{1,6}\s(.*?)'
    code_pattern = r'^\`{3}(.*?)\`{3}$'
    quote_pattern = r'^\>\s(.*?)'
    unordered_pattern = r'^\*|^\-\s(.*?)'
    ordered_pattern = r'^\d\.\s(.*?)'
    
    if re.match(heading_pattern, block):
        tmp = block[:6]
        head_num = tmp.count('#')
        return f'h{head_num}'
    elif re.match(code_pattern,block):
        return 'code'
    
    is_quote = True
    
    for line in block.split('\n'):
        if not re.match(quote_pattern,line):
            is_quote = False
    
    if is_quote:
        return 'quote'
    
    is_unordered_list = True
    
    for line in block.split('\n'):
        if not re.match(unordered_pattern, line):
            is_unordered_list = False
    
    if is_unordered_list:
        return 'unorderedlist'

    is_ordered_list = True
    i = 1
    
    for line in block.split('\n'):
        if re.match(ordered_pattern,line) and f'{i}' in line:
            i += 1
        else:
            is_ordered_list = False

    if is_ordered_list:
        return 'orderedlist'
        
    return 'paragraph'