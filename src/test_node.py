import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class TestNode(unittest.TestCase):
    def test_props_to_html_same(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        expected = ' href="https://www.google.com" target="_blank"'

        test = HTMLNode(None, None, None, props)
        self.assertEqual(expected, test.props_to_html())
    
    def test_props_to_html_diff(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        expected = ' href="https://www.google.com" target="_self"'

        test = HTMLNode(None, None, None, props)
        self.assertNotEqual(expected, test.props_to_html())
    
    def test_propper_print(self):
        expected = "HTMLNode: tag: div, value: Hello, children: None, props: {'class': 'my-class'}"
        test = HTMLNode("div", "Hello", None, {"class": "my-class"})
        self.assertEqual(expected, repr(test))
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_one_prop(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_two_prop(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)
    
    def test_diff_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "URL")
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_diff_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertIsNone(html_node.props)

    def test_italic_text(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertIsNone(html_node.props)
    
    def test_code_text(self):
        node = TextNode("print('hi')", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hi')")
        self.assertIsNone(html_node.props)

    def test_link_text(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image_text(self):
        node = TextNode("A bear", TextType.IMAGE, "https://example.com/bear.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/bear.png", "alt": "A bear"},
        )

    def test_invalid_type_raises(self):
        class FakeType:
            pass

        node = TextNode("oops", FakeType())
        with self.assertRaises(Exception):
            text_node_to_html_node(node)   

if __name__ == "__main__":
    unittest.main()