from textnode import *
from htmlnode import *

def main():
    textnode = TextNode("Some text", "bold", "www.me.com")
    htmlnode = HTMLNode("p","this is a paragraph text","test",{"href": "https://www.google.com","target": "_blank"})
    print(textnode)
    text = htmlnode.props_to_html()
    print(text)
main()