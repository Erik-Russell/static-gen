import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []
    escaped_delimiter = re.escape(delimiter)
    regex_string = f"{escaped_delimiter}(.+?){escaped_delimiter}"

    for node in old_nodes:
        start = 0
        matches = list(re.finditer(regex_string, node.text))

        print(matches)

        if not matches:
            new_nodes.append(TextNode(node.text, TextType.NORMAL))
            return new_nodes

        start = 0
        for match in matches:
            plain_text = node.text[start:match.start()]
            if plain_text:
                new_nodes.append(TextNode(plain_text, TextType.NORMAL))
            new_nodes.append(TextNode(match.group(1), text_type))
            start = match.end()

        remaining_plain_text = node.text[start:]
        if remaining_plain_text:
            new_nodes.append(TextNode(remaining_plain_text, TextType.NORMAL))

    return new_nodes