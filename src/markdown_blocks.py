from textnode import text_node_to_html
from split_node_delimiter import text_to_textnodes
from htmlnode import ParentNode, LeafNode, HTMLNode

import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH



def markdown_to_blocks(markdown):
    new_block = []

    section = markdown.split("\n\n")

    for line in section:
        if line == "":
            continue
        new_block.append(line.strip())
    return new_block


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        node = block_to_html_node(block)
        block_nodes.append(node)
    
    return ParentNode("div", block_nodes)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        children = text_to_children(block)
        return ParentNode("p", children)

    
    if block_type == BlockType.HEADING:
        level = 0
        for ch in block:
            if ch == "#":
                level += 1
            else:
                break
        text = block[level + 1 :].strip()
        children = text_to_children(text)
        return ParentNode(f"h{level}", children)

    if block_type == BlockType.CODE:
        lines = block.split("\n")
        text = "\n".join(lines[1:-1])
        code_node = LeafNode("code", text)
        return ParentNode("pre", [code_node])
        
        
def text_to_children(text):
    children = []
    textnode = text_to_textnodes(text)
    for node in textnode:
        children.append(text_node_to_html(node))
    return children





md = """
```
def text_to_children(text):
    children = []
    textnode = text_to_textnodes(text)
    for node in textnode:
        children.append(text_node_to_html(node))
    return children
```
"""
print(markdown_to_html_node(md))

