
from api.models import OperationLog
import datetime


class StorageStationService(object):
    '''
        Classe responsável pelas regras de negócio.
    '''
    percent_emit_warning_pickup = 80
    
    @staticmethod
    def is_almost_full(percent):
        if percent >= StorageStationService.percent_emit_warning_pickup:
            return True
        else:
            return False
    
    @staticmethod
    def perform_operation(storage_station, operation_detail):
        OperationLog.objects.create(storage_station=storage_station, operation_detail=operation_detail, operation_date=datetime.datetime.now())
