import unittest

from textnode import TextNode, TextType
from simplesplit import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode("This has normal text")
        new_node = split_nodes_delimiter([node], "**", TextType.NORMAL)
        self.assertEqual(new_node, [node])

    def test_bold_text(self):
        node = TextNode("This has **bold** text")
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_node[0].text, 'This has ')
        self.assertEqual(new_node[1].text_type, TextType.BOLD)
        self.assertEqual(new_node[1].text, 'bold')
        self.assertEqual(new_node[2].text, ' text')

    def test_bold_at_start(self):
        node = TextNode("**This starts** with bold text.")
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_node[0].text_type, TextType.BOLD)
        self.assertEqual(new_node[0].text, 'This starts')
        self.assertEqual(new_node[1].text, ' with bold text.')

    def test_bold_at_end(self):
        node = TextNode("This ends with **bold.**")
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_node[0].text, 'This ends with ')
        self.assertEqual(new_node[1].text_type, TextType.BOLD)
        self.assertEqual(new_node[1].text, 'bold.')

    def test_italic_text(self):
        node = TextNode("This has *italic* text")
        new_node = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_node[0].text, 'This has ')
        self.assertEqual(new_node[1].text_type, TextType.ITALIC)
        self.assertEqual(new_node[1].text, 'italic')
        self.assertEqual(new_node[2].text, ' text')

    def test_bad_markdown(self):
        node = TextNode("This has **bad markdown")
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_node, [node])

    def test_two_nodes(self):
        node_1 = TextNode("This is the **first** node.")
        node_2 = TextNode("And now we have the **second** node.")
        new_nodes = split_nodes_delimiter([node_1, node_2], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is the ")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "first")
        self.assertEqual(new_nodes[2].text, " node.")
        self.assertEqual(new_nodes[3].text, "And now we have the ")
        self.assertEqual(new_nodes[4].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[4].text, "second")
        self.assertEqual(new_nodes[5].text, " node.")

if __name__ == '__main__':
    unittest.main()