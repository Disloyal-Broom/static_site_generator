import re

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    results = re.findall(pattern, text)
    
    if results == []:
        return None
    else: 
        return results