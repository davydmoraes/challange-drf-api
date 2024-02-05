from django.urls import path, include
from rest_framework import routers
from .views import StorageStationList, StorageStationDetail, OperationLogList, OperationLogDetail, ChangeOccupiedPercentView, RequestPickupView, ConfirmPickupView


urlpatterns = [
    path('storage-station/list', StorageStationList.as_view()),
    path('storage-station/detail/<int:pk>', StorageStationDetail.as_view()),
    path('operation-log/list', OperationLogList.as_view()),
    path('operation-log/detail/<int:pk>', OperationLogDetail.as_view()),
    path('storage-station/<int:id>/percent/', ChangeOccupiedPercentView.as_view()),
    path('pickup/<int:id>/request', RequestPickupView.as_view()),
    path('pickup/<int:id>/confirm', ConfirmPickupView.as_view()),

]

