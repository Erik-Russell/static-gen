from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(node)

    p_node = HTMLNode(tag='p', value='This is a paragraph.', props={'class': 'text'})
    a_node = HTMLNode(tag='a', value='Google', props={'href': 'https://www.google.com'})
    div_node = HTMLNode(tag='div', children=[p_node, a_node])
    print(div_node)

if __name__ == '__main__':
    main()
