import unittest

from textnode import TextNode, DevilFruit


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", DevilFruit.LOGIA)
        node2 = TextNode("This is a text node", DevilFruit.LOGIA)
        self.assertEqual(node, node2)
    
    def test_diff_url(self):
        node = TextNode("This is a text node", DevilFruit.LOGIA, "URL")
        node2 = TextNode("This is a text node", DevilFruit.LOGIA)
        self.assertNotEqual(node, node2)

    def test_diff_text_type(self):
        node = TextNode("This is a text node", DevilFruit.ZOAN)
        node2 = TextNode("This is a text node", DevilFruit.LOGIA)
        self.assertEqual(node, node2)

    def assertEqual(self, node, node2):
        return node == node2
    
    def assertNotEqual(self, node, node2):
        return node != node2


if __name__ == "__main__":
    unittest.main()