from markdown_to_blocks import *
from block_to_block_type import * 
from text_to_textnodes import *
import re

def text_to_children(text):
        try:
            split_text = text.splitlines()
        except: 
            split_text = text
            
        node_list = []
        ol_detector = False
        ol_counter = 1

        for line in split_text:
            
            type = block_to_block_type(line)
            
            if ol_detector and re.match(r'^\d\.\s(.*?)$', line):
                ol_counter += 1
                type = 'orderedlist'
            else:
                ol_detector = False
                ol_counter = 1
       
            match(type):
                case 'h1':
                    node_list.append(TextNode(line, type, None))

                case 'h2':
                    node_list.append(TextNode(line, type, None))

                case 'h3':
                    node_list.append(TextNode(line, type, None))

                case 'h4':
                    node_list.append(TextNode(line, type, None))

                case 'h5':
                    node_list.append(TextNode(line, type, None))

                case 'h6':
                    node_list.append(TextNode(line, type, None))
                
                case 'quote':
                    node_list.append(TextNode(line, 'blockquote', None))
                
                case 'unorderedlist':
                    node_list.append(TextNode(line, 'ul', None))
                
                case 'orderedlist':
                    node_list.append(TextNode(line, 'ol', None))
                    ol_detector = True
                
                case 'code':
                    node_list.append(TextNode(line, type, None))
                
                case 'paragraph':
                    text_node = text_to_textnodes(line)
                    for node in text_node:
                        node_list.append(node)

        return node_list