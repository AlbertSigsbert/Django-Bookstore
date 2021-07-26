from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='book.index'),
    path('<int:id>', views.show, name='book.show')
]
