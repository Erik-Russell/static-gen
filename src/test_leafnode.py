import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        leaf = LeafNode(tag='p', value="This is a paragraph.", props={"class": "text"})
        self.assertEqual(leaf.tag, 'p')
        self.assertEqual(leaf.value, "This is a paragraph.")
        self.assertEqual(leaf.props, {"class": "text"})

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_class(self):
        node = LeafNode("h1", "Heading One", props = {'class': 'make_it_big'})
        self.assertEqual(node.to_html(), '<h1 class="make_it_big">Heading One</h1>')



if __name__ == "__main__":
    unittest.main()
