from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('add/',views.add,name = 'add'),
    path('delete/<int:num>',views.delete,name = 'delete'),
    path('edit/<int:num>',views.edit,name = 'edit'),
]