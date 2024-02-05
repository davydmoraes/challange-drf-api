from rest_framework import serializers
from .models import StorageStation, OperationLog
from .validators import *

class StorageStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageStation
        fields = '__all__'
        
class OperationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLog
        fields = '__all__'
