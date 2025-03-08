import unittest
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType

class TestParentNode(unittest.TestCase):
  def test_to_html_no_tag(self):
    node = ParentNode(None, [TextNode("test", TextType.TEXT)])
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_blank_tag(self):
    node = ParentNode("", [TextNode("test", TextType.TEXT)])
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_no_children(self):
    node = ParentNode("div", None)
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_empty_children(self):
    node = ParentNode("div", [])
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )

if __name__ == "__main__":
  unittest.main()
