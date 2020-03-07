from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Pharmacy
from .serializers import PharmacySerializer
from .forms import PharmacyForm

def user_input(request):
    print(request.method)
    if request.method == 'GET':
        pharmacy = Pharmacy.objects.all()
        return render(request, 'medicine/medicine.html', {'pharmacy': pharmacy})

    elif request.method == 'POST':
        pharmacy = get_object_or_404(Pharmacy, pk=request.POST.get("id"))
        form = PharmacyForm(request.POST, instance=pharmacy)

        if form.is_valid():
            member = form.save(commit=False)
            member.save()

        pharmacy = Pharmacy.objects.all()
        return render(request, 'medicine/medicine.html', {'pharmacy': pharmacy})
    

def pharmacy_list(request):
    if request.method == 'GET':
        pharmacy = Pharmacy.objects.all()
        
        serializer = PharmacySerializer(pharmacy, many=True)
        print(serializer)

        return JsonResponse(serializer.data, safe = False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        pharmacy_post = JSONParser().parse(request)
        serializer = PharmacySerializer(pharmacy_post)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.pharmacy, status=201)
        return JsonResponse(serializer.error, status=400)
