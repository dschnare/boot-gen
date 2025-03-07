import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_to_html_with_tag(self):
    node = LeafNode(tag = "div", value = "test")
    self.assertEqual(node.to_html(), "<div>test</div>")

    node = LeafNode(tag = "div", value = "test", props = {"class": "test"})
    self.assertEqual(node.to_html(), "<div class=\"test\">test</div>")

    node = LeafNode(tag = "div", value = "test", props = {"class": "test", "id": "test"})
    self.assertEqual(node.to_html(), "<div class=\"test\" id=\"test\">test</div>")

  def test_to_html_no_value(self):
    node = LeafNode(tag = "div")
    with self.assertRaises(ValueError):
      node.to_html()

  def test_to_html_no_tag(self):
    node = LeafNode(value = "test")
    self.assertEqual(node.to_html(), "test")

    node = LeafNode(value = "test", props = {"class": "test"})
    self.assertEqual(node.to_html(), "test")
      
      
    
if __name__ == "__main__":
  unittest.main()