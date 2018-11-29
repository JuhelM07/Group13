from django.contrib import admin
from tutorial import views
from django.conf.urls import url, include
from tutorial import views



urlpatterns = [
    url(r'^$', views.login_redirect, name= 'login_redirect'),
    url('admin/', admin.site.urls),
    url(r'^account/', include('account.urls', namespace='account'))
]
