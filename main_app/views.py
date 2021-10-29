from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView

from main_app.models import Widget
# Create your views here.
def home(request):
    return render(request, 'home.html')


class WidgetCreate(CreateView):
    description = Widget
    quantity = '__all__'

class WidgetDelete(DeleteView):
    description = Widget
    quantity = '__all__'
