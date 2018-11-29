from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name="account"

urlpatterns= [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name="account/login.html"), name="login"),
    url(r'^logout/$', LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    url(r'^register/$',views.register, name='register'),
    url(r'^profile/$', views.view_profile, name= 'view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name= 'edit_profile'),
    url(r'^change-password/$', views.change_password, name= 'change_password'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name="account/reset_password.html", email_template_name="account/reset_password_email.html"), name="reset_password"),
    url(r'^reset-password/done$', PasswordResetDoneView.as_view(template_name="account/reset_password_done.html"), name= 'password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,23})/$',
    PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    url(r'^reset-password/complete$', PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
]
