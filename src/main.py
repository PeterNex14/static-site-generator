from textnode import TextNode
from textnode import TextType

def main():
    bold = TextNode("This is bold text", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(bold)




if __name__ == "__main__":
    main()
