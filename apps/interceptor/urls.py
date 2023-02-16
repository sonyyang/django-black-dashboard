# -*- encoding: utf-8 -*-
from django.urls import path
from .views import address_view

urlpatterns = [
    path('address', address_view, name="address"),
]
