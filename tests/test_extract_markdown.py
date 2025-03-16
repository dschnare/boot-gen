import unittest
from boot_gen.extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
  def test_should_extract_markdown_images(self):
    self.assertEqual(extract_markdown_images("some text ![alt text](image.png) other text ![alt text](image2.png)"), [("alt text", "image.png"), ("alt text", "image2.png")])
    self.assertEqual(extract_markdown_images("some text other text"), [])

  def test_should_extract_markdown_links(self):
    self.assertEqual(extract_markdown_links("some text [link](https://example.com) other text ![alt text](https://example2.com)"), [("link", "https://example.com")])
    self.assertEqual(extract_markdown_links("some text other text"), [])

if __name__ == "__main__":
  unittest.main()
