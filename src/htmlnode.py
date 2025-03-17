class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        """
        string for HTML tag name (e.g. "p", "a", "h1")
        """

        self.value = value
        """
        string for value of HTML tag (e.g. text inside a p)
        """

        self.children = children if children is not None else []
        """
        list of HTMLNode obj that are the children of this node
        """

        self.props = props if props is not None else {}
        """
        Dictionary of key-value pairs representing the attributes of the HTML tag.
        For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        """

    def __repr__(self):
        props_str = self.props_to_html() if self.props else ''
        children_str = ', '.join(repr(child) for child in self.children) if self.children else ''

        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children=[{children_str}], props='{props_str}')"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ''
        output = ''
        for k, v in self.props.items():
            output += f' {k}="{v}"'
        return output


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        """
        Call the parent (HTMLNode) constructor using super() to initialize tag, value, and props.
        Ensure that children is always an empty list since this is a leaf node.
        """

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
