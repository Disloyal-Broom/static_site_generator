from leafnode import *
from parentnode import *

def leafnode_to_parentnode(leaf_nodes):
    if len(leaf_nodes) == 0:
        return ParentNode('div',None,None,None)
    
    parent = ParentNode('div', None, [], None)
    
    parent_node = []
    new_children = []

    for node in leaf_nodes:

        if node.tag == 'p' or node.tag == None:
            if new_children != []:
                parent_node.append(ParentNode(new_children[0].tag, new_children[0].value, new_children[1:]))
                new_children = []

        new_children.append(node)
    else:   
        new_children.append(node)

    if new_children:
        parent_node.append(new_children[0])
        
    for node in parent_node:
        parent.children.append(node)

    return parent


