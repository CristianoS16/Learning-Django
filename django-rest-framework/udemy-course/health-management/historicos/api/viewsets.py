from historicos.api.serializers import HistoricoSerializer
from historicos.models import Historicos
from rest_framework import viewsets


class HistoricosViewset(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('data')
    serializer_class = HistoricoSerializer
