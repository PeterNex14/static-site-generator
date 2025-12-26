
import unittest

from textnode import TextNode, TextType, text_node_to_html

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq_text_type(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("This is text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is text node, text, https://www.boot.dev)",
            repr(node)
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold_text(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")
    
    def test_italic_text(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")
    
    def test_code_text(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")
    
    def test_link_text(self):
        node = TextNode("This is link text", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is link text")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})
    
    def test_image_text(self):
        node = TextNode("This is image text", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is image text"})
        

if __name__ == "__main__":
    unittest.main()