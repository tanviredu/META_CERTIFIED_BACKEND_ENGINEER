from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt
def books(request):
    if request.method == "GET":
        bks = Book.objects.all().values()
        return JsonResponse({"books":list(bks)},safe=False)
    elif request.method == "POST":
        print(request.POST)
        title  = request.POST.get("title")
        author = request.POST.get("author")
        price       = request.POST.get("price")
        inventory   = request.POST.get("inventory")
        book        = Book()
        book.title  = title
        book.author = author
        book.price  = price
        book.inventory = inventory
        try:
            book.save()
            return JsonResponse(model_to_dict(book))
        except IntegrityError:
            return JsonResponse({"Error":"true","message":"required field Missing"})