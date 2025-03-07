import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    node = HTMLNode(None, None, None, props = {"class": "test", "id": "test"})
    self.assertEqual(node.props_to_html(), " class=\"test\" id=\"test\"")
  
  def test_props_to_html_empty(self):
    node = HTMLNode(None, None, None, props = {})
    self.assertEqual(node.props_to_html(), "")
    node = HTMLNode(None, None, None, None)
    self.assertEqual(node.props_to_html(), "")

  def test_repr(self):
    node = HTMLNode(None, None, None, props = {"class": "test", "id": "test"})
    self.assertEqual(repr(node), "HTMLNode(None, None, None, {'class': 'test', 'id': 'test'})")

if __name__ == "__main__":
  unittest.main()
