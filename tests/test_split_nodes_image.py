import unittest
from boot_gen.textnode import TextNode, TextType
from boot_gen.split_nodes_image import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
  def test_should_not_split_nodes_when_node_is_empty(self):
    nodes = [TextNode("", TextType.TEXT)]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(new_nodes, [TextNode("", TextType.TEXT)])

  def test_should_not_split_nodes_image_when_no_image_found(self):
    nodes = [TextNode("Hello, world!", TextType.TEXT)]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(new_nodes, [TextNode("Hello, world!", TextType.TEXT)])

  def test_should_split_image_nodes(self):
    nodes = [TextNode("Hello, world![yep](  nope ![alt image](image.png)", TextType.TEXT)]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(new_nodes, [
      TextNode("Hello, world![yep](  nope ", TextType.TEXT),
      TextNode("alt image", TextType.IMAGE, "image.png")
    ])

  def test_should_split_image_when_no_text_before_image(self):
    nodes = [TextNode("![alt image](image.png)", TextType.TEXT)]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(new_nodes, [
      TextNode("alt image", TextType.IMAGE, "image.png")
    ])

  def test_should_splits_multiple_images(self):
    nodes = [TextNode("Hello, world! ![alt image](image.png) and [another image](image2.png)!", TextType.TEXT)]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(new_nodes, [
      TextNode("Hello, world! ", TextType.TEXT),
      TextNode("alt image", TextType.IMAGE, "image.png"),
      TextNode(" and [another image](image2.png)!", TextType.TEXT)
    ])


if __name__ == "__main__":
  unittest.main()
