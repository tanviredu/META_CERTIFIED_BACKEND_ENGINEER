from django.shortcuts import render
from django.db import InterfaceError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt
def books(request):
    if request.method == "GET":
        bks = Book.objects.all().values()
        return JsonResponse({"books":list(bks)},safe=False)