"""
@author xy
@time 7/17/2018
"""

from rest_pandas.renderers import PandasExcelRenderer


class CustomExcelRenderer(PandasExcelRenderer):
    def get_pandas_kwargs(self, data, renderer_context):
        return {'index': False}


class CustomCSVRenderer(PandasExcelRenderer):
    def get_pandas_kwargs(self, data, renderer_context):
        return {'index': False}
