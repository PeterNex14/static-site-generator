from textnode import TextType, TextNode
from utils import split_nodes_delimiter
import unittest


class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is a `code block` word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE), 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code block", TextType.CODE), 
                TextNode(" word", TextType.TEXT),
            ]
        )
    
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is a **bold text** word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD), 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD), 
                TextNode(" word", TextType.TEXT),
            ]
        )
    
    def test_split_nodes_delimiter_bold_doubled(self):
        node = TextNode("This is a **bold text** word and another **bold text**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD), 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD), 
                TextNode(" word and another ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
            ]
        )
    
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is a _italic text_ word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "_", TextType.ITALIC), 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic text", TextType.ITALIC), 
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_nodes_delimiter_italic_and_bold(self):
        node = TextNode("This is a _italic text_ word and **bold text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic text", TextType.ITALIC), 
                TextNode(" word and ", TextType.TEXT),
                TextNode("bold text", TextType.BOLD),
            ]
        )
    
    def test_split_nodes_delimiter_no_close_delimiter(self):
        node = TextNode("This is a _italic text word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()