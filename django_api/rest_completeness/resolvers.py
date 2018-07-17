"""
@author xy
@time 7/17/2018
"""

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_pandas import PandasSimpleView
from functools import partial
import pandas as pd

from .models import *
from ..utils import check_required_params_in_request, get_completeness, response_file
from .renderers import *


class CompletenessStatsList(APIView):
    parser_classes = [JSONParser]

    def get(self, request, format=None):
        query_params = request.query_params

        if not check_required_params_in_request(query_params, ['date']):
            return Response('date is required in request', status=status.HTTP_400_BAD_REQUEST)

        _get_completeness = partial(get_completeness, 'all_stats', query_params['date'])

        if 'id' in query_params:
            query_result = _get_completeness(id=query_params['id'])
        elif 'trader' in query_params:
            query_result = _get_completeness(trader=query_params['trader'])
        else:
            query_result = _get_completeness()

        serializer = CompletenessStatsSerializer(query_result, many=True)
        return Response(serializer.data)


class CompletenessDetailList(APIView):
    parser_classes = [JSONParser]

    def get(self, request, format=None):
        query_params = request.query_params

        _check = not any([
            check_required_params_in_request(query_params, ['date', 'id']),
            check_required_params_in_request(query_params, ['date', 'trader'])
        ])

        if _check:
            return Response('date and (id or trader) are required in request', status=status.HTTP_400_BAD_REQUEST)

        _get_completeness = partial(get_completeness, 'all_detail', query_params['date'])

        if 'id' in query_params:
            query_result = _get_completeness(id=query_params['id'])
        elif 'trader' in query_params:
            query_result = _get_completeness(trader=query_params['trader'])
        else:
            raise Exception('check input')

        serializer = CompletenessDetailSerializer(query_result, many=True)
        return Response(serializer.data)


class TestDownLoadExcel(PandasSimpleView):
    renderer_classes = [CustomExcelRenderer]

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        filename = query_params['filename'] if 'filename' in query_params else 'TestDownLoadExcel'

        foo = pd.DataFrame({
            'name': ['Jacob', 'Neo'],
            'score': [5, 3]
        })
        return response_file(foo, filename, 'xlsx')


class TestDownLoadCSV(PandasSimpleView):
    renderer_classes = [CustomCSVRenderer]

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        filename = query_params['filename'] if 'filename' in query_params else 'TestDownLoadExcel'

        foo = pd.DataFrame({
            'name': ['Jacob', 'Neo'],
            'score': [5, 3]
        })
        return response_file(foo, filename, 'csv')
