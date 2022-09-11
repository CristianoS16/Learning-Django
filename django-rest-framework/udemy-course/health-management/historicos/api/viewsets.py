from historicos.api.serializers import (HistoricoDetalhesSerializer,
                                        HistoricoSerializer)
from historicos.models import Historicos
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class HistoricosViewset(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('data')
    serializer_class = HistoricoSerializer

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Historicos.objects.filter(pk=pk)
        self.serializer_class = HistoricoDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
