from django.urls import URLPattern, path, include
from .views import CustomerListView


urlpatterns = [
    path("customer-list", CustomerListView.as_view(), name="customerlist"),
]
