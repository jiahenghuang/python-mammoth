from . import documents


def paragraph(transform_paragraph):
    def transform_element(element):
        if isinstance(element, documents.Paragraph):
            return transform_paragraph(element)
        else:
            return element
    
    return _each_element(transform_element)


def _each_element(transform_element):
    def transform_element_and_children(element):
        if isinstance(element, documents.HasChildren):
            children = list(map(transform_element, element.children))
            element = element.copy(children=children)
        
        return transform_element(element)
    
    return transform_element_and_children
