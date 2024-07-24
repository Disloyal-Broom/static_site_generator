from leafnode import *
from textnode import *

def text_node_to_html_node(text_node):

    match(text_node.text_type):
        
        case "text":
            return LeafNode('p',text_node.text)
        
        case "bold":
            return LeafNode('strong',text_node.text)
        
        case "code":
            return LeafNode('code',text_node.text)
        
        case "link":
            return LeafNode('link',text_node.text,{'href':f'{text_node.url}'})
        
        case "image":
            return LeafNode('image','',{'src':f'{text_node.url}', 'alt':f'{text_node.text}'})
        
        case 'h1':
            return LeafNode('h1', text_node.text, None)

        case 'h2':
            return LeafNode('h2', text_node.text, None)

        case 'h3':
            return LeafNode('h3', text_node.text, None)

        case 'h4':
            return LeafNode('h4', text_node.text, None)

        case 'h5':
            return LeafNode('h5', text_node.text, None)

        case 'h6':
            return LeafNode('h6', text_node.text, None)
        
        case 'blockquote':
            return LeafNode('blockquote', text_node.text, None)
        
        case 'unorderedlist':
            return LeafNode('ul', text_node.text, None)
        
        case 'orderedlist':
            return LeafNode('ol', text_node.text, None)
        
        case 'paragraph':
            return LeafNode('p', text_node.text, None)
        
        case 'italics':
            return LeafNode('em', text_node.text, None)
        
        case _:
            raise Exception(f'TextNode_Type: {text_node.text_type} not found.')