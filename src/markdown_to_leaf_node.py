from markdown_to_blocks import *
from textnode_to_htmlnode import *
from text_to_children import *

def markdown_to_leaf_node(markdown):

    blocks = markdown_to_blocks(markdown)
    text_nodes = text_to_children(blocks)
    leaf_nodes = []
    
    for node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(node))
    
    return leaf_nodes

markdown_to_leaf_node("# This is heading1\n## This is heading2\n### This is heading3\n\n> quote quote\n> quote")