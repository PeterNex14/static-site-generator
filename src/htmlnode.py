from enum import Enum


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        
        list_props = []
        for key, value in self.props.items():
            list_props.append(f' {key}="{value}"')

        return "".join(list_props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Value cannot be None")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag cannot be None")

        if self.children == None:
            raise ValueError("Children cannot be None")

        children = ""
        for child in self.children:
            children += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"