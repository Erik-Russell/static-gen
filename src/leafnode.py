from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=[], props=None):
        if not value:
            raise ValueError("A 'value' is required for LeafNode.")

        super().__init__(tag=tag, value=value, children=[], props=props)
        """
        Call the parent (HTMLNode) constructor using super() to initialize tag, value, and props.
        Ensure that children is always an empty list since this is a leaf node.
        """

    def to_html(self):
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
