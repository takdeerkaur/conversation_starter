from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from topics import views

urlpatterns = [
	url(r'^$', views.api_root),
    url(r'^topics/$', views.TopicList.as_view(), name='topic-list'),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view(), name='topic-detail'),
    url(r'^topics/random/$', views.RandomTopic.as_view(), name='random-topic'),
    url(r'^topics/category/(?P<category>\w+)/$', views.TopicListByCategory.as_view(), name='topic-list-by-category'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
