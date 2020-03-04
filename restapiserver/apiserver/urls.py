from django.contrib import admin
from django.urls import path, include
from main.views import data_list
from medicine.views import pharmacy_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_list),
    path('p/', pharmacy_list),
]