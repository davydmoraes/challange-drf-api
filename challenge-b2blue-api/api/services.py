
class StorageStationService(object):
    percent_emit_warning_pickup = 80
    
    @staticmethod
    def is_almost_full(percent):
        if percent >= StorageStationService.percent_emit_warning_pickup:
            return True
        else:
            return False