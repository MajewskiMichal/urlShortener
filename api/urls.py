from django.urls import path
from .views import AddressCreate, AddressDetailView

urlpatterns = [
    path('', AddressCreate.as_view(), name='shortener-create'),
    path('<pk>', AddressDetailView.as_view(), name='shortener-detail'),
]