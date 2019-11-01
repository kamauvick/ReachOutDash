import graphene

import reachweb.schema


class Query(reachweb.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
