class HTMLNode:
  def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict | None = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html must be implemented by subclasses")
  
  def props_to_html(self):
    if self.props is None or len(self.props) == 0:
      return ""
    else:
      return " " + " ".join([f"{k}=\"{v}\"" for k, v in self.props.items()])

  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

