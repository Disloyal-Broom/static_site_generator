from markdown_to_blocks import *
from block_to_block_type import * 
from split_nodes_image import *
from split_nodes_link import *
from htmlnode import *

def text_to_children(text):

        type = block_to_block_type(text)
        
        match(type):
            case 'h1':
                return HTMLNode(type, text, None, None)

            case 'h2':
                return HTMLNode(type, text, None, None)

            case 'h3':
                return HTMLNode(type, text, None, None)

            case 'h4':
                return HTMLNode(type, text, None, None)

            case 'h5':
                return HTMLNode(type, text, None, None)

            case 'h6':
                return HTMLNode(type, text, None, None)
            
            case 'quote':
                return HTMLNode('blockquote', text, None, None)
            
            case 'unorderedlist':
                return HTMLNode('ul', text, None, None)
            
            case 'orderedlist':
                return HTMLNode('ol', text, None, None)
            
            case 'code':
                return HTMLNode(type, text, None, None)
            
            case 'paragraph':
                return HTMLNode('p', text, None, None)
            
            case _:
                return split_nodes_link(split_nodes_image(text))