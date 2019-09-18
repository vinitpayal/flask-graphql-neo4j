from py2neo import Graph
from py2neo.ogm import Property
from graphql import GraphQLError

from models import base


class Person(base.BaseModel):
    __primarykey__ = 'IdObject'
    IdObject = Property()
    Name = Property()
    NameFamily = Property()
    NameFull = Property()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def as_dict(self):
        return {
            'user_name': self.IdObject,
            'first_name': self.Name,
            'last_name': self.NameFamily,
            'full_name': self.NameFull
        }
    
    def fetch(self):
        graph = base.get_graph_obj()

        person = self.match(graph).where(IdObject=self.IdObject).first()

        if person is None:
            raise GraphQLError(f'"{self.IdObject}" has not been found in our employee list.')
        
        return person
