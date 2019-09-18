from py2neo.ogm import GraphObject, Property, RelatedTo
from py2neo import Graph


def get_graph_obj():
    graph = Graph()
    return graph

class BaseModel(GraphObject):
    """
    Implements some basic functions to guarantee some standard functionality
    across all models. The main purpose here is also to compensate for some
    missing basic features that we expected from GraphObjects, and improve the
    way we interact with them.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def all(self):
        return self.select(graph)

    def save(self):
        graph.push(self)

