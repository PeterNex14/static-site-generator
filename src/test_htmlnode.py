import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import markdown_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("div", "Google", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Google")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})

    def test_eq_props_to_html(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_eq_props_to_html_no_props(self):
        node = HTMLNode("a", "Google", None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode("p", "Google", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode(p, Google, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_to_html_raise_exception(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )   

    def test_to_html_with_none_tag(self):
        node = ParentNode(None, [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_none_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an ordered list
2. with items
3. and more items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an ordered list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a\nblockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
        