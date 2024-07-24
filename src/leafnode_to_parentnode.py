from leafnode import *
from parentnode import *

def leafnode_to_parentnode(leaf_nodes):
    
    parent_node = []
    new_children = leaf_nodes[1:]
    
    if len(new_children) - 1 == 0:
        return parent_node.append(leaf_nodes[0])
        
    if leaf_nodes[0].tag == 'p' or leaf_nodes[0].tag == None:
        
        tag_list = []
        for children in new_children:
            tag_list.append(children.tag)
            
        if leaf_nodes[0].tag in tag_list:
            parent_node.append(ParentNode(leaf_nodes[0].tag, leaf_nodes[0].value, leafnode_to_parentnode(new_children)))
            
        else:
            return parent_node.append(leaf_nodes[0])
            
    else:   
        parent_node.append(leaf_nodes[0])
        parent_node.append(leafnode_to_parentnode(new_children))
        
    print(parent_node)
    return parent_node


