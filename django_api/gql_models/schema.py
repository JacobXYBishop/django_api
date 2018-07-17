"""
@author xy
@time 7/14/2018
"""

import graphene
import logging

from .resolvers import resolve_all_stats, resolve_all_detail
from .models import ModelsAllDetail, ModelsAllStats

_logger = logging.getLogger(__name__)


class ModelsAllStatsQuery(graphene.ObjectType):
    toy_models_all_stats = graphene.Field(
        type=graphene.List(ModelsAllStats),
        description='模型统计信息',
        symbols=graphene.Argument(graphene.List(graphene.String), required=True, description='代码'),
        resolver=resolve_all_stats
    )


class ModelsAllDetailQuery(graphene.ObjectType):
    toy_models_all_detail = graphene.Field(
        type=graphene.List(ModelsAllDetail),
        description='模型详细信息',
        symbols=graphene.Argument(graphene.List(graphene.String), required=True, description='代码'),
        # start_date=graphene.Argument(graphene.String, description='起始日'),
        # end_date=graphene.Argument(graphene.String, description='结束日'),
        resolver=resolve_all_detail
    )
