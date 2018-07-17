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

    return pd.read_sql(
        """
        SELECT
        date,
        symbol,
        open,
        high,
        low,
        close,
        change_rate,
        upper,
        middle,
        lower,
        signal,
        position,
        capital_return,
        capital
        FROM signal_boll
        WHERE symbol in ('{}')
        """.format(symbols),
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

    return pd.read_sql(
        """
        SELECT
        symbol,
        annual_return,
        cumulative_returns,
        annual_volatility,
        sharpe_ratio,
        calmar_ratio,
        stability,
        max_drawdown,
        omega_ratio,
        sortino_ratio,
        skew,
        kurtosis,
        tail_ratio,
        daily_value_at_risk,
        alpha,
        beta
        FROM signal_boll_stats
        WHERE symbol in ('{}')
        """.format(symbols),
        __ENGINE
    )
