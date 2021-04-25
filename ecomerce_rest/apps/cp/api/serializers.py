from rest_framework import serializers
from apps.cp.models import cp 

class cpSerializer(serializers.ModelSerializer):
    class Meta:
        model = cp
        fields = ('id', 'codigo', 'colonia', 'd_tipo_asenta', 'municipio', 'estado', 'ciudad')

        