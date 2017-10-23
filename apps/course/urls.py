from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create', views.create),
    url(r'^(?P<course_id>\d+)/confirm', views.confirm),
    url(r'^(?P<course_id>\d+)/delete', views.delete)
]