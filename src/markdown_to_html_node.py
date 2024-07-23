from markdown_to_blocks import *
from text_to_children import *
from split_nodes_image import *
from split_nodes_link import *

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks: 
        nodes.append(text_to_children(block))

    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    print(nodes)

markdown_to_html_node("![link](link.com)\n#This is heading1\n## This is heading2\n### This is heading3")