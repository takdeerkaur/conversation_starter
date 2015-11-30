from topics import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

urlpatterns = patterns('',
    url(r'^admin/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include('topics.urls')),
)
