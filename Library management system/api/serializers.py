from rest_framework import serializers
from library.models import newsmodel

class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsmodel
        fields = '__all__'