"""
@author xy
@time 7/17/2018
"""

from rest_framework import serializers


class CompletenessStatsSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    trader = serializers.CharField(max_length=255)
    volume_weighted = serializers.FloatField()
    pre_amount_weighted = serializers.FloatField()
    amount_weighted = serializers.FloatField()

    _timestamp = serializers.IntegerField()


class CompletenessDetailSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    trader = serializers.CharField(max_length=255)
    symbol = serializers.CharField(max_length=255)
    volume_instruction = serializers.IntegerField(),
    volume_transaction = serializers.IntegerField(),
    complete_rate = serializers.FloatField(),
    abs_volume = serializers.IntegerField(),
    pre_close = serializers,
    close = serializers.FloatField(),
    pre_amount = serializers.FloatField(),
    amount = serializers.FloatField()

    _timestamp = serializers.IntegerField()
