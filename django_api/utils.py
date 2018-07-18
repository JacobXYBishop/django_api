"""
@author xy
@time 7/17/2018
"""

import pandas as pd
from functools import partial
from rest_framework.response import Response
from influxdb import DataFrameClient

__INFLUX = DataFrameClient('10.144.64.85', 8086, 'trading', '123456', 'trading')


def _date2timestamp(date):
    return int(pd.Timestamp(date).to_datetime64())


def check_required_params_in_request(query_params, params_list):
    """

    :param query_params:
    :param params_list:
    :return:
    """
    qp = query_params.keys()
    its = set.intersection(set(qp), set(params_list))
    return its == set(params_list)


def get_completeness(db, date, **kwargs):
    """

    :param db:
    :param date:
    :param kwargs:
    :return:
    """
    que_str = 'select * from {} where time = {}'.format(db, _date2timestamp(date))
    for i in kwargs:
        que_str += " and {} = '{}'".format(i, kwargs[i])
    # print(que_str)
    que = __INFLUX.query(que_str)
    if que:
        return que[db].to_dict(orient='records')
    return []


def response_file(df, filename, extension):
    """

    :param df:
    :param filename:
    :param extension:
    :return:
    """
    res = Response(df)
    res['Content-Disposition'] = 'attachment; filename={}.{}'.format(filename, extension)
    return res


def _to_object(x, model, **kwargs):
    result = model()
    [setattr(result, i, x.get(i, None)) for i in kwargs.get('_projections')]
    return result


def handle_resolver(model):
    """
    用于简化resolver的装饰器：
        1. 从resolver info提取所需返回数据信息用于构件projections
        2. http response根据resolver返回类型进行赋值
    :param model:
    :return:
    """

    def _decorator(func):
        def _wrapper(obj, info, **kwargs):
            _projections = [
                x.name.value for x in
                info.operation.selection_set.selections[0].selection_set.selections
            ]

            _apply_func = partial(_to_object, model=model, _projections=_projections)

            func_return = func(obj, info, _projections=_projections, **kwargs)

            if isinstance(func_return, pd.DataFrame):
                return func_return.apply(_apply_func, axis=1).tolist()

            if isinstance(func_return, list):
                return map(_apply_func, func_return)

            raise Exception('function return only accepts DataFrame or list')

        return _wrapper

    return _decorator
