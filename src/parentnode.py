from htmlnode import *
from leafnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__()
        self.children = children
        self.tag = tag
        self.props = props
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: Tag is empty.")
        elif self.children == None or self.children == []:
            raise ValueError("Error: Children is empty.")
        
        return_string = f'<{self.tag}>'
      
        for html_item in self.children:
            return_string += html_item.to_html()
            
        return_string += f'</{self.tag}>'
        
        return return_string
            
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'