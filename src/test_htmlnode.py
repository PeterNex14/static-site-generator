import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        