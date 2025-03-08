import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    a = TextNode("Hello, world!", TextType.TEXT, None)
    b = TextNode("Hello, world!", TextType.TEXT)
    self.assertEqual(a, b)

  def test_ne(self):
    a = TextNode("Hello, world!", TextType.TEXT, None)
    b = TextNode("Hello, world!", TextType.LINK, "https://www.google.com")
    self.assertNotEqual(a, b)
  
  def test_repr(self):
    a = TextNode("Hello, world!", TextType.LINK, "https://www.google.com")
    self.assertEqual(str(a), "TextNode(Hello, world!, link, https://www.google.com)")

if __name__ == "__main__":
  unittest.main()
