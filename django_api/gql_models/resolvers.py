"""
@author xy
@time 7/14/2018
"""

import pandas as pd
import sqlalchemy as sa

from .models import ModelsAllStats, ModelsAllDetail
from ..utils import handle_resolver

__ENGINE = sa.create_engine('postgresql://admin:admin@10.144.64.68:5432/toymodels')


@handle_resolver(ModelsAllDetail)
def resolve_all_detail(obj, info, **kwargs):
    """

    :param obj:
    :param info:
    :param kwargs:
    :return:
    """
    symbols = ','.join(kwargs.get('symbols'))
    selections = ','.join(kwargs.get('_projections'))

    return pd.read_sql(
        """
        SELECT
        {}
        FROM signal_boll
        WHERE symbol in ('{}')
        """.format(selections, symbols),
        __ENGINE
    )


@handle_resolver(ModelsAllStats)
def resolve_all_stats(obg, info, **kwargs):
    """

    :param obg:
    :param info:
    :param kwargs:
    :return:
    """
    symbols = ','.join(kwargs.get('symbols'))
    selections = ','.join(kwargs.get('_projections'))

    return pd.read_sql(
        """
        SELECT
        {}
        FROM signal_boll_stats
        WHERE symbol in ('{}')
        """.format(selections, symbols),
        __ENGINE
    )
