from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ClientList.as_view(), name='client_list'),
    path('add_client', views.ClientCreate.as_view(), name='client_create'),
    path('<int:pk>/update_client', views.ClientUpdate.as_view(), name='client_update'),
    path('<int:pk>/delete_client', views.ClientDelete.as_view(), name='client_delete'),
    path('<int:pk>/', views.ClientDetail.as_view(), name='client_detail'),
    path('<int:pk>/add_category', views.CategoryCreate.as_view(), name='category_create'),
    path('<int:client_id>/<int:pk>/update_category', views.CategoryUpdate.as_view(), name='category_update'),
    path('<int:client_id>/<int:pk>/delete_category', views.CategoryDelete.as_view(), name='category_delete'),
    path('<int:client_id>/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('<int:client_id>/<int:pk>/add_document', views.DocumentCreate.as_view(), name='document_create'),
    path('<int:client_id>/<int:category_id>/<int:pk>/update_document', views.DocumentUpdate.as_view(), name='document_update'),
    path('<int:client_id>/<int:category_id>/<int:pk>/delete_document', views.DocumentDelete.as_view(), name='document_delete'),
    path('<int:client_id>/<int:category_id>/<int:pk>/', views.DocumentDetail.as_view(), name='document_detail'),
    path('<int:client_id>/<int:category_id>/<int:pk>/add_step', views.StepCreate.as_view(), name='step_create'),
    path('<int:client_id>/<int:category_id>/<int:document_id>/<int:pk>/update_step', views.StepUpdate.as_view(), name='step_update'),
    path('<int:pk>/delete_step', views.StepDelete.as_view(), name='step_delete'),
    path('<int:pk>/render/pdf/', views.Pdf.as_view(), name='generate_pdf'),
]
