from textnode import TextNode
from textnode import TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for nodes in old_nodes:

        if nodes.text_type != TextType.TEXT:
            new_nodes.append(nodes)
            continue

        if nodes.text.count(delimiter) != 2:
            raise Exception("invalid markdown syntax")
        
        text_split = nodes.text.split(delimiter)
        
        for i in range(len(text_split)):
            if i % 2 != 0:
                new_nodes.append(TextNode(text_split[i], text_type))
            else:
                new_nodes.append(TextNode(text_split[i], TextType.TEXT))    

    return new_nodes



node = TextNode("This is a _italic block_ word", TextType.TEXT)
print(split_nodes_delimiter([node], "_", TextType.ITALIC))
