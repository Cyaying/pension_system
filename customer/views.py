from django.views.generic import ListView
from django.shortcuts import render
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomerListView(ListView):
    template_name = 'customer/customer_list.html'
    model = Customer
    context_object_name = "Customer"
