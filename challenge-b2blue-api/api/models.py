from django.db import models

class StorageStation(models.Model):
    WASTE_TYPES = (
        ("PA", "Paper"),
        ("GL", "Glass"),
        ("PL", "Plastic"),
        ("ME", "Metal"),
        ("OR", "Organic"),
        ("WO", "Wood"),
        ("NR", "Non-Recyclable"),
    )
    occupied_storage_percent = models.IntegerField(default=0, null=False)
    waste_type = models.CharField(max_length=2, choices=WASTE_TYPES, blank=False, null=False)
    was_pickup_requested = models.BooleanField(default=False)        
    
    
class OperationLog(models.Model):
    operation_detail = models.CharField(max_length=100)
    storage_station = models.ForeignKey(StorageStation, on_delete=models.CASCADE)
    operation_date = models.DateTimeField()
    
    def __str__(self):
        return f"Estação de Armazenamento: {self.storage_station}. Data: {self.operation_date}. Operação: {self.operation_detail}."