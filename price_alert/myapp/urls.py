from django.urls import path
from .views import Home, AlertCreate, AlertList, AlertDelete
from .views import BitcoinPriceAlert


urlpatterns = [
    path('', Home.as_view()),
    path('alerts/create/', AlertCreate.as_view()),
    path('alerts/list/', AlertList.as_view()),
    path('alerts/delete/<uuid:pk>/', AlertDelete.as_view()),
    path('bitcoin-price/', BitcoinPriceAlert.as_view(), name='bitcoin-price'),

]
