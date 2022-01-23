from rest_framework import serializers
from dias_api.apps.Dias.models import Dia

class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia
        fields = '__all__'

