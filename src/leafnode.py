from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__()
        self.value = value
        self.tag = tag
        self.props = props
        
    def to_html(self):
        if self.value == None:
            raise Exception(ValueError)
        
        match(self.tag):
            
            case None:
                return f"{self.value}"
            case 'a':
                return self.props_to_html()
            case _:
                return f'<{self.tag}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'