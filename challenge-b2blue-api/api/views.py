import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import StorageStation, OperationLog
from rest_framework.views import APIView
from rest_framework import status, generics
from .serializers import StorageStationSerializer, OperationLogSerializer
from rest_framework.response import Response
from.services import StorageStationService


class OperationLogList(generics.ListCreateAPIView):
    queryset = OperationLog.objects.all()
    serializer_class = OperationLogSerializer

class OperationLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OperationLog.objects.all()
    serializer_class = OperationLogSerializer

class StorageStationList(generics.ListCreateAPIView):
    queryset = StorageStation.objects.all()
    serializer_class = StorageStationSerializer

class StorageStationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StorageStation.objects.all()
    serializer_class = StorageStationSerializer
    
class ChangeOccupiedPercentView(APIView):
    """
        Responsável pela edição da porcentagem ocupada de uma estação de armazenamento.
    """
    def put(self, request, id):
   
        body = json.loads(request.body)
        new_percent = body.get('occupied_storage_percent')
        
        storage_station = get_object_or_404(StorageStation, pk=id)
        serializer = StorageStationSerializer(storage_station, data=request.data, partial=True)
     
        if serializer.is_valid() & serializer.validate_occupied_storage_percent(new_percent):
            StorageStationService.perform_operation(storage_station, f"Mudança na % de volume para {new_percent}")
            is_almost_full = StorageStationService.is_almost_full(new_percent)
            
            if is_almost_full:
                message = f"A estação está quase cheia! O volume atual é de {storage_station.occupied_storage_percent}%. Foi solicitada uma coleta para a estação {storage_station.id}!"
                storage_station.occupied_storage_percent = new_percent
                serializer.save()
                
                return Response({'message': message, 'data': serializer.data, 'status': status.HTTP_207_MULTI_STATUS})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestPickupView(APIView):
    '''
        Realiza solicitação do recolhimento de uma estação.
    '''
    def put(self, request, id):
        storage_station = get_object_or_404(StorageStation, pk=id)
        serializer = StorageStationSerializer(storage_station, data=request.data, partial=True)
        
        if serializer.is_valid():
            StorageStationService.perform_operation(storage_station, f"A coleta para a estação {storage_station.id} foi solicitada.")
            storage_station.was_pickup_requested = True
            storage_station.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConfirmPickupView(APIView):
    '''
        Responsável por confirmar o recolhimento em uma estação.
    '''
    def put(self, request, id):
        storage_station = get_object_or_404(StorageStation, pk=id)
        serializer = StorageStationSerializer(storage_station, data=request.data, partial=True)
        
        if serializer.is_valid():
            StorageStationService.perform_operation(storage_station, f"Coleta relizada na estação {storage_station.id}.")
            storage_station.occupied_storage_percent = 0
            storage_station.was_pickup_requested = False
            storage_station.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
