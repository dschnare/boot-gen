from .textnode import TextNode, TextType

# def split_nodes_image(old_nodes):
#   new_nodes = []

#   for node in old_nodes:
#     if node.text_type != TextType.TEXT:
#       new_nodes.append(node)
#       continue

#     parts = node.text.split("![")

#     if len(parts) == 1:
#       new_nodes.append(node)
#       continue

#     text_part = parts[0]

#     for part in parts[1:]:
#       subparts = part.split("](", maxsplit=1)

#       if len(subparts) == 2 and subparts[0].find("]") == -1 and subparts[1].find(")") != -1:
#         if text_part != "":
#           new_nodes.append(TextNode(text_part, TextType.TEXT))

#         frags = subparts[1].split(")")
#         new_nodes.append(TextNode(subparts[0], TextType.IMAGE, frags[0]))
#         text_part = ")".join(frags[1:])

#         if text_part != "":
#           new_nodes.append(TextNode(text_part, TextType.TEXT))
        
#         text_part = ""
#       else:
#         text_part += "![" + part
    
#     if text_part != "":
#       new_nodes.append(TextNode(text_part, TextType.TEXT))

#   return new_nodes


def split_nodes_image(old_nodes):
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

    last_image_end = 0
    current_image_start = -1

    while (i < _len):
      c = node.text[i]

      if c == '!' and lookahead("!["):
        current_image_start = i
        i += 2
        alt_text = ""
        image_url = ""

        while (i < _len):
          c = node.text[i]

          if c == ']':
            break

          if c == '!' and lookahead("!["):
            break

          alt_text += c
          i += 1
        
        if c == ']' and lookahead("]("):
          i += 2

          while (i < _len):
            c = node.text[i]

            if c == ')':
              break

            if c == '!' and lookahead("!["):
              break

            image_url += c
            i += 1

          if c == ')':
            if current_image_start - last_image_end > 0:
              new_nodes.append(TextNode(node.text[last_image_end:current_image_start], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            last_image_end = i + 1
            i += 1
      else:
        i += 1
    
    if current_image_start == -1:
      new_nodes.append(node)
    elif last_image_end < _len:
      new_nodes.append(TextNode(node.text[last_image_end:], TextType.TEXT))

  return new_nodes
