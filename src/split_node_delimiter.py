from textnode import *

delimiter_to_text_type = {
    #'#':'heading1', # single delim
    #'##':'heading2', # single delim
    #'###':'heading3', # single delim
    #'####':'heading4', # single delim
    #'#####':'heading5', # single delim
    #'\n':'break', # single delim
    '__':'bold',
    '**':'bold',
    '*':'italics',
    '_':'italics',
    '***':'bold&italics',
    '___':'bold&italics',
    #'>':'blockquote', single delim
    #TODO: add order list functionality r'number':'list'
    #'-':'unorderedlist', # single delim
    #'+':'unorderedlist', # single delim
    #'* ':'unorderedlist', # single delim
    #'\t*':'unorderedlist', # single delim
    "'":'code',
    #'[]':'linktext', # changing delim
    #'()':'linkurl', # changing delim
    #'<>':'link', # changing delim
    '':'text'
    }


#TODO: figure out how to handle single delimiters ex. \n, ordered lists, etc...
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    
    for node in old_nodes:
        
        if node.text != '':
            text = node.text
            
            if node.text_type == 'link' or node.text_type == 'image':
                node_list.append(node)
            else:  
                try: 
                    delim_index = text.index(delimiter)
                    before_delim = text[:delim_index]

                    try: 
                        delim_index_close = text[delim_index + len(delimiter):].index(delimiter)
                    except:
                        continue

                    if before_delim != '':
                        node_list.append(TextNode(before_delim, text_type, node.url))

                    if delim_index_close:
                        between_delim = text[delim_index + len(delimiter): ( len(delimiter)) + delim_index + delim_index_close]
                        node_list.append(TextNode(between_delim, delimiter_to_text_type[delimiter], node.url))
                        remaining_text = text[( 2 * len(delimiter)) + delim_index + delim_index_close:]
                    else:
                        remaining_text = text[( 2 * len(delimiter)) + delim_index:]

                    if(remaining_text != ''):
                        node_list.append(TextNode(remaining_text, text_type, node.url))

                except:
                    node_list.append(node)

        else: 
            node_list.append(node)

    return node_list