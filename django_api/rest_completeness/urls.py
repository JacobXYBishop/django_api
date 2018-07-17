"""
@author xy
@time 7/17/2018
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .resolvers import *

urlpatterns = {
    url(
        r'^completeness_stats/$',
        CompletenessStatsList.as_view(),
        name="completeness_stats"
    ),
    url(
        r'^completeness_detail/$',
        CompletenessDetailList.as_view(),
        name="completeness_detail"
    ),
    url(
        r'^test_excel/$',
        TestDownLoadExcel.as_view(),
        name="test_excel"
    ),
    url(
        r'^test_csv/$',
        TestDownLoadCSV.as_view(),
        name="test_csv"
    ),
}

urlpatterns = format_suffix_patterns(urlpatterns)
