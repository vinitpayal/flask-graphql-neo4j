from graphene import ObjectType, String, Schema, Field
from flask_graphql import GraphQLView
from flask import Flask

from models.person import Person

class PersonSchema(ObjectType):
    user_name = String()
    first_name = String()
    last_name = String()
    full_name = String()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.person = Person(IdObject=self.user_name).fetch()
    
    # def resolve_full_name(parent, info):
    #     print(parent)
    #     return f"{parent.first_name} {parent.last_name}"

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    person = Field(lambda: PersonSchema,  user_name=String(default_value="cbartens"))
    
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'
    
    def resolve_person(root, info, **kwargs):
        user_name = kwargs['user_name']
        print(user_name)
        person = Person(IdObject=user_name).fetch()
        return PersonSchema(**person.as_dict())

        # return PersonSchema(**kwargs)
        # print(kwargs)
        # return kwargs


schema = Schema(query=Query)

# query_string = '{ hello(name: "Vinit") }'
# result = schema.execute(query_string)
# print(result.data['hello'])

app = Flask(__name__)
app.debug = True                

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()