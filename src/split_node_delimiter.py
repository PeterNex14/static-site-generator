
from extract_md import extract_markdown_images, extract_markdown_links
from textnode import TextNode
from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for nodes in old_nodes:

        if nodes.text_type != TextType.TEXT:
            new_nodes.append(nodes)
            continue

        split_nodes = []
        sections = nodes.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue

            if i % 2 != 0:
                new_nodes.append(TextNode(sections[i], text_type))
            else:
                new_nodes.append(TextNode(sections[i], TextType.TEXT))  

        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            new_nodes.append(nodes)
            continue

        split_nodes = []

        extracted_image = extract_markdown_images(nodes.text)

        if len(extracted_image) == 0:
            new_nodes.append(nodes)
            continue

        original_text = nodes.text
        
        for image_alt, image_link in extracted_image:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(sections) != 2:
                raise ValueError("Invalid markdown, image not found")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            
            original_text = sections[1]

        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            new_nodes.append(nodes)
            continue

        extracted_links = extract_markdown_links(nodes.text)

        if len(extracted_links) == 0:
            new_nodes.append(nodes)
            continue

        original_text = nodes.text
        
        for link_alt, link_link in extracted_links:
            sections = original_text.split(f"[{link_alt}]({link_link})", 1)

            if len(sections) != 2:
                raise ValueError("Invalid markdown, link not found")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_link))
            
            original_text = sections[1]

        
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    
    return new_nodes
