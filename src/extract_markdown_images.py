import re

def extract_markdown_images(text):
    results = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    if results == []:
        return None
    else: return results
