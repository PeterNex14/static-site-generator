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

