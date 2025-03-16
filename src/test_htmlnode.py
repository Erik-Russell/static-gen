import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag='p', value='This is a paragraph.', children=[], props={'class': 'text'})
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'This is a paragraph.')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class': 'text'})

    def test_init_empty_child_and_props(self):
        node = HTMLNode(tag='p', value='This is a paragraph.')
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'This is a paragraph.')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_repr_with_child_and_prop(self):
        p_node = HTMLNode(tag='p', value='This is a paragraph.', props={'class': 'text'})
        a_node = HTMLNode(tag='a', value='Google', props={'href': 'https://www.google.com'})
        div_node = HTMLNode(tag='div', children=[p_node, a_node])

        expected_repr = (
            "HTMLNode(tag='div', value='None', children=[HTMLNode(tag='p', value='This is a paragraph.', children=[], props=' class=\"text\"'), "
            "HTMLNode(tag='a', value='Google', children=[], props=' href=\"https://www.google.com\"')], props='')"
        )
        self.assertEqual(repr(div_node), expected_repr)

    def test_repr_whith_no_child_or_props(self):
        node = HTMLNode(tag='p', value='Just text.')
        expected_repr = "HTMLNode(tag='p', value='Just text.', children=[], props='')"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node = HTMLNode(tag='a', value='Click me', props={'href': 'https://boot.dev', 'target': '_blank'})
        expected_props = ' href="https://boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_with_no_props(self):
        node = HTMLNode(tag='p', value='No props here')
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()
