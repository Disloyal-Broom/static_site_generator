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
    "```":'code',
    '`': 'code'
    }

def text_to_textnodes(text):
    node = split_nodes_delimiter([TextNode(text,'text')],'','text')
    node_list = split_nodes_image(node)
    node_list = split_nodes_link(node_list)

    for key in delimiter_to_text_type.keys():
            node_list = split_nodes_delimiter(node_list, key, 'text')

    return node_list  
