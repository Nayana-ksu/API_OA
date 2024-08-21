# api/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Item

class ItemList(View):
    def get(self, request):
        items = Item.objects.all().values('id', 'name', 'description')
        return JsonResponse(list(items), safe=False)

class ItemDetail(View):
    def get(self, request, pk):
        item = Item.objects.filter(pk=pk).values('id', 'name', 'description').first()
        if item:
            return JsonResponse(item)
        return JsonResponse({'error': 'Item not found'}, status=404)
