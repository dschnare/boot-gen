import unittest
from boot_gen.textnode import TextNode, TextType
from boot_gen.split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
  def test_should_not_split_nodes_when_node_is_empty(self):
    nodes = [TextNode("", TextType.TEXT)]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(new_nodes, [TextNode("", TextType.TEXT)])

  def test_should_not_split_nodes_link_when_no_link_found(self):
    nodes = [TextNode("Hello, world!", TextType.TEXT)]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(new_nodes, [TextNode("Hello, world!", TextType.TEXT)])
  
  def test_should_handle_broken_link_markup(self):
    nodes = [TextNode("Hello, world![yep](  nope [link text](theurl)", TextType.TEXT)]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(new_nodes, [
      TextNode("Hello, world![yep](  nope ", TextType.TEXT),
      TextNode("link text", TextType.LINK, "theurl")
    ])

  def test_should_skip_images(self):
    nodes = [TextNode("Hello, world![yep](image.png)  nope [link text](theurl)", TextType.TEXT)]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(new_nodes, [
      TextNode("Hello, world![yep](image.png)  nope ", TextType.TEXT),
      TextNode("link text", TextType.LINK, "theurl")
    ])
  
  def test_should_split_multiple_links(self):
    nodes = [TextNode("Hello, world! ![alt image](image.png) with a [link](a url) and [another image](image2.png)!", TextType.TEXT)]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(new_nodes, [
      TextNode("Hello, world! ![alt image](image.png) with a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "a url"),
      TextNode(" and ", TextType.TEXT),
      TextNode("another image", TextType.LINK, "image2.png"),
      TextNode("!", TextType.TEXT)
    ])


if __name__ == "__main__":
  unittest.main()
