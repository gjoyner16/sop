from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from docs import views
from accounts.views import change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ClientList.as_view(), name='client_list'),
    path('accounts/', include('accounts.urls')),
    path('docs/', include('docs.urls')),
    path('password/', change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
