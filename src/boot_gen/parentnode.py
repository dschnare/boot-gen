from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag: str, children: list, props: dict | None = None):
    super().__init__(tag, None, children, props)
    
  def to_html(self):
    if self.tag is None or self.tag == "":
      raise ValueError("Tag is required for parent nodes")
    
    if self.children is None or len(self.children) == 0:
      raise ValueError("Children are required for parent nodes")
    
    return f"<{self.tag}{self.props_to_html()}>{"".join([child.to_html() for child in self.children])}</{self.tag}>"
