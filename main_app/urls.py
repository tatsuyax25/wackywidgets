from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widgets/create/', views.add_widget, name='widgets_create'),
    path('widgets/delete/<int:widget_id>', views.delete_widget, name='widgets_delete'),
]