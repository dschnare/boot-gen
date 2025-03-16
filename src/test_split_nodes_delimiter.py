import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_should_not_split_when_delimiter_not_found(self):
    nodes = [TextNode("Hello, world!", TextType.TEXT)]
    new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    self.assertEqual(new_nodes, [TextNode("Hello, world!", TextType.TEXT)])

  def test_should_split_when_delimiter_found(self):
    nodes = [TextNode("Hello, **world**!", TextType.TEXT)]
    new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    self.assertEqual(new_nodes, [TextNode("Hello, ", TextType.TEXT), TextNode("world", TextType.BOLD), TextNode("!", TextType.TEXT)])

  def test_should_raise_error_when_delimiter_is_unbalanced(self):
    nodes = [TextNode("Hello, **world!", TextType.TEXT)]
    with self.assertRaises(ValueError):
      split_nodes_delimiter(nodes, "**", TextType.BOLD)

if __name__ == "__main__":
  unittest.main()
