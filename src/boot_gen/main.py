from .textnode import TextNode, TextType

def main():
  text_node = TextNode("Hello, world!", TextType.LINK, "https://www.google.com")
  print(text_node)

if __name__ == "__main__":
  main()
