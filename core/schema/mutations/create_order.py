from graphene import Mutation, String, Field
from core.schema.queries import OrderNode


class CreateOrder(Mutation):
    class Arguments:
        name = String(required=True)

    ok = String

    def mutate(root, info, name):
        print("MUTATE")
        return CreateOrder(ok="True")
