from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('detail/<int:document_id>', views.detail, name='detail'),
    path('detail/<int:document_id>/add_step', views.add_step, name='add_step'),
]
