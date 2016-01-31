from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from categories import views

urlpatterns = [
	url(r'^$', views.api_root),
    url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name='category-detail'),
    url(r'^categories/(?P<category>\w+)/$', views.CategoryIdByNameList.as_view(), name='category-name-by-id'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
