from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag: str | None = None, value: str | None = None, props: dict | None = None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("All leaf nodes must have a value")
    
    if self.tag is None:
      return f"{self.value}"

    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
