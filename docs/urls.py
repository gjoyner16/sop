from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('client/<int:clientfolder_id>', views.client, name='client'),
    path('client/category/<int:categoryfolder_id>', views.category, name='category'),
    path('detail/<int:document_id>', views.detail, name='detail'),
    path('detail/<int:document_id>/add_step', views.add_step, name='add_step'),
]
