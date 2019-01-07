from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from front_app.utils import query_get_all

class Memegen(View):
    def get(self, request):
        return HttpResponse("OK")

class Home(View):
    def get(self, request):
        return HttpResponse("OK")

class Listing(View):
    def get(self, request):
        listing_items = query_get_all()
        return render(request, template_name='listing.html', context={'listing_items': listing_items})