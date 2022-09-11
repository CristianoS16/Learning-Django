from historicos.models import Historicos
from imagens.api.serializers import ImagensHistoricosSerializer
from rest_framework import serializers


class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'


class HistoricoDetalhesSerializer(serializers.ModelSerializer):

    imagens = ImagensHistoricosSerializer(many=True, read_only=True)

    class Meta:
        model = Historicos
        fields = [
            'id_historico',
            'data',
            'aparecimento_sintomas',
            'duracao',
            'local_dor',
            'tipo_dor',
            'conclusao',
            'id_agendamento',
            'imagens'
        ]
