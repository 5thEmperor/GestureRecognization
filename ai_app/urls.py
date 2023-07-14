from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index),
    path('face-count/', facefun),
    path('virtual/', virtualfun),
    path('key/',virtualkey)
    # path('keyboard/', keyboardfun),


]
