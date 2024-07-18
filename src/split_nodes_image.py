from extract_markdown_images import *
from textnode import *

def split_nodes_image(oldnode):
    new_node_list = []

    for i in range(len(oldnode)):
        manip_text = oldnode[i].text
        markdown_images = extract_markdown_images(manip_text)

        if markdown_images == None:
            new_node_list.append(TextNode(manip_text, oldnode[i].text_type, oldnode[i].url))
        else:
            for image_links in range(len(markdown_images)):

                index = manip_text.index('![')
                before_link_text = manip_text[:index]
                
                if before_link_text != '':
                    new_node_list.append(TextNode(before_link_text,oldnode[i].text_type, oldnode[i].url))
                
                new_node_list.append(TextNode(markdown_images[image_links][0], 'image', markdown_images[image_links][1]))
            
                if '](' in manip_text and ')' in manip_text:
                    text_after_link_start = manip_text[index:]
                    index_of_closing_link = text_after_link_start.index(')')
                    text_after_link = text_after_link_start[index_of_closing_link + 1 :]

                    if text_after_link != '' and '![' not in text_after_link:
                        new_node_list.append(TextNode(text_after_link, oldnode[i].text_type, oldnode[i].url))         
                    else: 
                        manip_text = text_after_link
    return new_node_list
