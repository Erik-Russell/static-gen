import unittest

from textnode import TextNode, TextType
from typing import cast
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, 'https://boot.dev')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_to_html_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = cast(LeafNode, text_node.text_node_to_html_node())
        self.assertEqual(leaf_node.value, 'This is a text node')
        self.assertEqual(leaf_node.tag, 'b')
        self.assertEqual(leaf_node.to_html(), '<b>This is a text node</b>')

    def test_text_to_html_text(self):
        text_node = TextNode("This is a text node")
        leaf_node = cast(LeafNode, text_node.text_node_to_html_node())
        self.assertEqual(leaf_node.to_html(), 'This is a text node')
    
    def test_text_to_html_italic(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        leaf_node = cast(LeafNode, text_node.text_node_to_html_node())
        self.assertEqual(leaf_node.to_html(), '<i>This is a text node</i>')

    def test_text_to_html_code(self):
        text_node = TextNode("This is a text node", TextType.CODE)
        leaf_node = cast(LeafNode, text_node.text_node_to_html_node())
        self.assertEqual(leaf_node.to_html(), '<code>This is a text node</code>')

    def test_text_to_html_link(self):
        text_node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        leaf_node = cast(LeafNode, text_node.text_node_to_html_node())
        self.assertEqual(leaf_node.to_html(), '<a href="https://boot.dev">This is a link</a>')

    def test_text_to_html_image(self):
        text_node = TextNode("This is alt text", TextType.IMAGE, "https://boot.dev")
        leaf_node = cast(LeafNode, text_node.text_node_to_html_node())
        self.assertEqual(leaf_node.to_html(), '<img src="https://boot.dev" alt="This is alt text"></img>')

if __name__ == "__main__":
    unittest.main()
