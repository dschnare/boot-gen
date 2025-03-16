from textnode import TextNode, TextType

def split_nodes_link(old_nodes):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != TextType.TEXT or node.text == "":
      new_nodes.append(node)
      continue

    _len = len(node.text)
    i = 0

    def lookahead(text):
      nonlocal i
      nonlocal _len
      nonlocal node
      l = len(text)

      if i + l > _len:
        return False

      return text == node.text[i:i+l]

    last_link_end = 0
    current_link_start = -1

    while (i < _len):
      c = node.text[i]

      if c == '!' and lookahead("!["):
        i += 2
        continue
      
      if c == '[':
        current_link_start = i
        i += 1
        link_text = ""
        link_url = ""

        while (i < _len):
          c = node.text[i]

          if c == ']':
            break

          if c == '!' and lookahead("!["):
            break

          link_text += c
          i += 1
        
        if c == ']' and lookahead("]("):
          i += 2

          while (i < _len):
            c = node.text[i]

            if c == ')':
              break

            if c == '!' and lookahead("!["):
              break

            link_url += c
            i += 1

          if c == ')':
            if current_link_start - last_link_end > 0:
              new_nodes.append(TextNode(node.text[last_link_end:current_link_start], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            last_link_end = i + 1
            i += 1
      else:
        i += 1
    
    if current_link_start == -1:
      new_nodes.append(node)
    elif last_link_end < _len:
      new_nodes.append(TextNode(node.text[last_link_end:], TextType.TEXT))

  return new_nodes
