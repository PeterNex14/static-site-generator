import unittest
from markdown_extractor import extract_title

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Heading"), "Heading")

    def test_extract_title_fails(self):
        with self.assertRaises(Exception):
            extract_title("Heading")

        with self.assertRaises(Exception):
            extract_title("## Heading")
        
        with self.assertRaises(Exception):
            extract_title("### Heading")

        with self.assertRaises(Exception):
            extract_title("#Heading")

if __name__ == '__main__':
    unittest.main()
    