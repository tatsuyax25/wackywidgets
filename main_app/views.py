from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .form import WidgetForm
from main_app.models import Widget
# Create your views here.
def home(request):
    widget_form = WidgetForm(request.POST)
    widgets = Widget.objects.all()
    return render(request, 'home.html', {'widget_form': widget_form, 'widgets': widgets})



def add_widget(request):
    	# create the ModelForm using the data in request.POST
  form = WidgetForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_widget = form.save(commit=False)
    new_widget.save()
  return redirect('home')

def delete_widget(request, widget_id):
    w = Widget.objects.get(id=widget_id)
# This will delete the Blog and all of its Entry objects.
    w.delete()
    	# create the ModelForm using the data in request.POST
    return redirect('home')