class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        
        html_string = ""

        for prop in self.props:
            att = self.props[prop].replace('"', '&quot;')
            html_string += f' {prop}="{att}"'
        
        return html_string
    
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props_to_html()}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, children = None, props = props)
    
    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError()
        if self.tag == None:
            return self.value

        if self.props is None or self.props == {}:
            html_string = f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return html_string