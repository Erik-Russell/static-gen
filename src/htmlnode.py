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
        output = ''
        for k, v in self.props.items():
            output += f' {k}="{v}"'
        return output
