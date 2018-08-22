from django.contrib import admin
from django.urls import path, include
from docs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('docs/', include('docs.urls')),
]
