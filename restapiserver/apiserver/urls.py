from django.contrib import admin
from django.urls import path, include
from main.views import data_list
from medicine.views import pharmacy_list, user_input

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_input),
    path('m/', data_list),
    path('p/', pharmacy_list),
]