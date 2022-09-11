from imagens.api.serializers import ImagensHistoricosSerializer
from imagens.models import ImagensHistorico
from rest_framework import viewsets


class ImagensHistoricosViewset(viewsets.ModelViewSet):
    queryset = ImagensHistorico.objects.all()
    serializer_class = ImagensHistoricosSerializer
