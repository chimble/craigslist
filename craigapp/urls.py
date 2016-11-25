from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
import craigapp


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^create_user/$', craigapp.views.create_user, name='create_user'),
    url(r'^accounts/profile/$', craigapp.views.profile_view, name='user_profile'),
    url(r'^index$', views.index, name='index'),
]
