from imagens.models import ImagensHistorico
from rest_framework import serializers


class ImagensHistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensHistorico
        fields = '__all__'
