from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^login/$', views.user_login, name="login"),  #login view of first lesson
    url(r'^login/$', auth_views.login, name='login'),   #login view of second lesson
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_change/$', auth_views.password_change, {"post_change_redirect":"/account/password_change_done"}, name="password_change"),
    url(r'^password_change_done/$', auth_views.password_change_done, name="password_change_done"),
    url(r'^register/$', views.register, name="register"),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^upload_img/$', views.upload_img, name='upload_img'),
]