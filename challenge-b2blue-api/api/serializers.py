from rest_framework import serializers
from .models import StorageStation, OperationLog
from .validators import *

class StorageStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageStation
        fields = '__all__'
        
    def validate_occupied_storage_percent(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("A porcentagem precisa ser um número inteiro.")
        return value
            
class OperationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLog
        fields = '__all__'
