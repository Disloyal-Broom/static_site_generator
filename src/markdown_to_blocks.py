def markdown_to_blocks(md_text):
    block = md_text.split('\n')
    new_blocks = []
    for i in range(len(block)):

        if block[i].strip() == '' or block[i].isspace():
            continue
        else: 
            new_blocks.append(block[i])

    return new_blocks