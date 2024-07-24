from markdown_to_blocks import *
from textnode_to_htmlnode import *
from text_to_children import *

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    text_nodes = text_to_children(blocks)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    
    for node in html_nodes:
        print(node)
        
    return html_nodes

markdown_to_html_node("# This is heading1\n## This is heading2\n### This is heading3\n\n> quote quote\n> quote")