from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from docs.views import ClientList

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('edit_user', views.edit_user, name='user'),
    path('', ClientList.as_view(), name='client_list'),
    path('password_reset', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
