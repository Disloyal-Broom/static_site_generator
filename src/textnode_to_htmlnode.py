from leafnode import *
from textnode import *

def text_node_to_html_node(text_node):
    
    match(text_node.text_type):
        
        case "text":
            return LeafNode(None,text_node.text)
        
        case "bold":
            return LeafNode('b',text_node.text)
        
        case "italic":
            return LeafNode('i',text_node.text)
        
        case "code":
            return LeafNode('code',text_node.text)
        
        case "link":
            return LeafNode('link',text_node.text,{'href':f'{text_node.url}'})
        
        case "image":
            return LeafNode('image','',{'src':f'{text_node.url}', 'alt':f'{text_node.text}'})
        
        case _:
            raise Exception('TextNode_Type not found.')