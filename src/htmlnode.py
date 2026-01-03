class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("function not implemented")
    
    def props_to_html(self):
        html = ""
        for prop in self.props:
            html += f" {prop}=\"{self.props[prop]}\""
        return html
    
    def __repr__(self):
        return f"HTMLNode: tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return value
        
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children")
        
        new_tag = ""
        for child in self.children:
            new_tag += child.to_html()
        
        if self.props == None:
            return f"<{self.tag}>{new_tag}</{self.tag}>"
        return f"<{self.tag}{super().props_to_html()}>{new_tag}</{self.tag}>"
