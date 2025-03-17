import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_init(self):
        child = LeafNode(tag='span', value='Leaf Node 1', props={'class': 'leaf'})
        node = ParentNode(tag='div', children=[child], props={'class': 'parent'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.children, [child])
        self.assertEqual(node.props, {'class': 'parent'})

    def test_to_html_with_children(self):
        child_node = LeafNode('span', 'child')
        parent_node = ParentNode(tag='div', children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode('span', [grandchild_node])
        parent_node = ParentNode(tag="div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode('span', 'child')
        child_node2 = LeafNode('span', 'child2')
        parent_node = ParentNode('div', [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child2</span></div>")

    def test_to_html_with_multiple_children_w_props(self):
        child_node = LeafNode('span', 'child', {'class': 'leaf'})
        child_node2 = LeafNode('span', 'child2')
        parent_node = ParentNode('div', [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), '<div><span class="leaf">child</span><span>child2</span></div>')

    def test_to_html_with_multiple_children_parent_w_props(self):
        child_node = LeafNode('span', 'child')
        child_node2 = LeafNode('span', 'child2')
        parent_node = ParentNode('div', [child_node, child_node2], {'class': 'parent'})
        self.assertEqual(parent_node.to_html(), '<div class="parent"><span>child</span><span>child2</span></div>')

if __name__ == "__main__":
    unittest.main()
