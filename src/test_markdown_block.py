import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        

    def test_block_to_block_type_heading(self):
        md = "# This is heading"
        md_heading_2 = "## This is heading 2"
        md_heading_3 = "### This is heading 3"
        md_heading_4 = "#### This is heading 4"
        md_heading_5 = "##### This is heading 5"
        md_heading_6 = "###### This is heading 6"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md_heading_2), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md_heading_3), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md_heading_4), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md_heading_5), BlockType.HEADING)
        self.assertEqual(block_to_block_type(md_heading_6), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        md = "```\nThis is code block\n```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_to_block_type_code_fails(self):
        md = "```This is code block"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        md = ">This is quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    
    def test_block_to_block_type_quote_with_space(self):
        md = "> This is quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    
    def test_block_to_block_type_unordered_list(self):
        md = "- This is unordered list"
        md_2 = "- This is unordered list\n- This is another unordered list"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(md_2), BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_unordered_list_fails(self):
        md = "-This is unordered list"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
    
    def test_block_to_block_type_ordered_list(self):
        md = "1. This is ordered list"
        md_2 = "1. This is ordered list\n2. This is ordered list"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(md_2), BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_ordered_list_fails(self):
        md = "1 This is ordered list"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        md = "This is paragraph"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
