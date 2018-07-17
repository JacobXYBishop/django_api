"""
@author xy
@time 7/17/2018
"""

import graphene

from .gql_models.schema import ModelsAllStatsQuery, ModelsAllDetailQuery

_queries = [
    ModelsAllStatsQuery,
    ModelsAllDetailQuery,
]


class Query(*_queries):
    """
    This class will inherit from multiple Queries
    as we begin to add more apps to our project
    """
    pass


schema = graphene.Schema(query=Query)
