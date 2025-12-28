# Static Site Generator

This is a custom-built static site generator written in Python. It takes raw Markdown content and converts it into a full HTML website, styling it with CSS and organizing it into a directory structure ready for deployment.

## Boot.dev Guided Project

This project was built as part of the "Build a Static Site Generator" course on [Boot.dev](https://www.boot.dev). It is a hands-on guided project designed to teach the fundamentals of text processing, recursion, and object-oriented programming in Python.

## What I've Learned

Through building this project, I've gained experience in:

*   **Recursion**: Using recursive functions to crawl directory trees, copy static files, and generate pages for nested content.
*   **Text Processing**: Parsing raw Markdown text, identifying syntax patterns (like bold, links, images), and converting them into structured HTML.
*   **Object-Oriented Programming**: Designing classes (`HTMLNode`, `LeafNode`, `ParentNode`, `TextNode`) to represent the DOM structure and separate concerns.
*   **Unit Testing**: Writing comprehensive unit tests using Python's `unittest` framework to verify the correctness of the parsing logic.
*   **Regular Expressions**: Using regex to robustly match Markdown patterns like images, links, and ordered lists.
*   **File I/O**: Reading from and writing to the file system to manage content, templates, and the public output directory.

## Key Concepts

*   **Node Representation**: The core design relies on representing HTML elements as nodes in a tree data structure.
    *   `TextNode`: Represents intermediate markdown text elements.
    *   `HTMLNode` (and subclasses): Represents the final HTML structure.
*   **Pipeline Processing**: The conversion process follows a pipeline:
    1.  **Markdown -> TextNodes**: Splitting text by delimiters (bold, italic, code).
    2.  **TextNodes -> HTMLNodes**: Converting processed text into HTML leaf nodes.
    3.  **Blocks -> HTMLTree**: Grouping text into blocks (paragraphs, lists, headings) and assembling the full HTML tree.
*   **Separation of Content and Logic**: The content lives in separate Markdown files, while the generator logic and HTML templates are kept distinct, allowing for easy updates and scalability.

## Architecture

The generator follows a straightforward data pipeline:

1.  **Input**:
    *   `content/`: Contains the raw Markdown files representing the pages.
    *   `static/`: Contains static assets like images and CSS.
    *   `template.html`: The base HTML shell that wraps the generated content.
2.  **Processing** (`src/`):
    *   The script cleans the output directory.
    *   It recursively copies all files from `static/` to the output directory.
    *   It crawls the `content/` directory. For each Markdown file, it:
        *   Parses the Markdown into "Blocks" (paragraphs, headings, lists).
        *   Parses inline text into "TextNodes" (bold, italic, links).
        *   Converts these structures into an `HTMLNode` tree.
        *   Renders the tree to an HTML string.
        *   Injects the HTML content and title into the `template.html`.
3.  **Output**:
    *   The fully rendered site is written to the `docs/` (or `public/`) directory, ready to be served by a web server.

## Future Improvements

Features I plan to add in the future:

*   **Support for more Markdown features**: Tables, footnotes, and task lists.
*   **Syntax Highlighting**: Adding a library to highlight code blocks automatically.
*   **RSS Feed Generation**: Automatically creating an RSS feed for the blog posts.
*   **Command Line Interface (CLI)**: Improving the arguments handling to make it a more robust CLI tool.
*   **Deployment Script**: Adding scripts to automatically deploy the `public` directory to GitHub Pages or AWS S3.
