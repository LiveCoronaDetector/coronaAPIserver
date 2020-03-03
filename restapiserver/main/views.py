from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Data
from .serializers import DataSerializer

def data_list(request):
    if request.method == 'GET':
        data = Data.objects.all()
        print(data)
        serializer = DataSerializer(data, many=True)
        print(serializer)
        print(serializer.data)
        # print(dir(serializer.data))
        print(dir(serializer))

        # print(list(serializer.data[0]))
        # for i in list(serializer.data[0]):
            
        
        # return HttpResponse(serializer.data)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data_post = JSONParser().parse(request)
        serializer = DataSerializer(data_post)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)