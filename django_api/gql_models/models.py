"""
@author xy
@time 7/14/2018
"""

import graphene


class ModelsAllDetail(graphene.ObjectType):
    """
    模型明细信息-返回数据类型
    """

    date = graphene.String(description='日期')
    symbol = graphene.String(description='代码')
    open = graphene.Float(description='开盘价')
    high = graphene.Float(description='最高价')
    low = graphene.Float(description='最低价')
    close = graphene.Float(description='收盘价')
    change_rate = graphene.Float(description='涨跌幅', name='change_rate')
    upper = graphene.Float(description='布林上')
    middle = graphene.Float(description='布林中')
    lower = graphene.Float(description='布林下')
    signal = graphene.Int(description='信号')
    position = graphene.Int(description='仓位')
    capital_return = graphene.Float(description='日收益', name='capital_return')
    capital = graphene.Float(description='累计收益')


class ModelsAllStats(graphene.ObjectType):
    """
    模型统计信息-返回数据类型
    """

    symbol = graphene.String(description='代码')
    annual_return = graphene.Float(description='年化', name='annual_return')
    cumulative_returns = graphene.Float(description='累计年化', name='cumulative_returns')
    annual_volatility = graphene.Float(description='波动率（年）', name='annual_volatility')
    sharpe_ratio = graphene.Float(description='sharpe', name='sharpe_ratio')
    calmar_ratio = graphene.Float(description='calmar', name='calmar_ratio')
    stability = graphene.Float(description='稳定性')
    max_drawdown = graphene.Float(description='最大回撤', name='max_drawdown')
    omega_ratio = graphene.Float(description='omega', name='omega_ratio')
    sortino_ratio = graphene.Float(description='sortino', name='sortino_ratio')
    skew = graphene.Float(description='偏度')
    kurtosis = graphene.Float(description='峰度')
    tail_ratio = graphene.Float(description='峰尾比', name='tail_ratio')
    daily_value_at_risk = graphene.Float(description='每日风险价值', name='daily_value_at_risk')
    alpha = graphene.Float(description='alpha')
    beta = graphene.Float(description='beta')
