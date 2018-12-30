from django.http import HttpResponse
from django.views import View

class Memegen(View):
    def get(self, request):
        return HttpResponse("OK")

class Home(View):
    def get(self, request):
        return HttpResponse("OK")
