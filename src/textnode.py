from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type=TextType.NORMAL, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text, self.text_type, self.url) == (other.text, other.text_type, other.url)
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type.value == 'normal':
            return LeafNode(tag=None, value=self.text)
        elif self.text_type.value == 'bold':
            return LeafNode('b', self.text)
        elif self.text_type.value == 'italic':
            return LeafNode('i', self.text)
        elif self.text_type.value == 'code':
            return LeafNode('code', self.text)
        elif self.text_type.value == 'link':
            return LeafNode('a', self.text, props={'href': self.url})
        elif self.text_type.value == 'image':
            return LeafNode('img', value='', props={'src': self.url, 'alt': self.text}) 
