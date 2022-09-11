from historicos.models import Historicos
from rest_framework import serializers


class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'
