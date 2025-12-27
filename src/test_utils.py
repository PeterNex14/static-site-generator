from textnode import TextType, TextNode
from split_node_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_links
from extract_md import extract_markdown_images, extract_markdown_links
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

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ]
        )

    def test_extract_markdown_links(self):
        text = "This is text with a [link to boot dev](https://www.boot.dev) and [link to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("link to boot dev", "https://www.boot.dev"),
                ("link to youtube", "https://www.youtube.com/@bootdotdev"),
            ]
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()