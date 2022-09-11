from agendamentos.models import Agendamentos
from historicos.api.serializers import HistoricoSerializer
from rest_framework import serializers


class AgendamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'


class AgendamentosDetalhesSerializer(serializers.ModelSerializer):
    historicos = HistoricoSerializer(many=True, read_only=True)

    class Meta:
        model = Agendamentos
        fields = [
            "id_agendamento",
            "data_hora",
            "data_criacao",
            "cancelado",
            "observacao",
            "tipo",
            "historicos"
        ]
