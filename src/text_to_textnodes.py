from split_node_delimiter import *
from split_nodes_image import *
from split_nodes_link import *

delimiter_to_text_type = {
    '***':'bold&italics',
    '___':'bold&italics',
    '__':'bold',
    '**':'bold',
    '*':'italics',
    '_':'italics',
    "'":'code',
    }

def text_to_textnodes(text):
    node = split_nodes_delimiter([TextNode(text,'text')],'','text')
    print(f'original_node: {node}')
    
    node_list = split_nodes_image(node)
    print(f'image_node: {node_list}')
    
    node_list = split_nodes_link(node_list)
    print(f'link node: {node_list}')
    for key in delimiter_to_text_type.keys():
            node_list = split_nodes_delimiter(node_list, key, 'text')

    for node in node_list:
        print(node)
    return node_list  

test_case = text_to_textnodes('here is an ![image](image.com), and a [link](link.com).')