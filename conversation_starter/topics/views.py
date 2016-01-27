import random
from topics.models import Topic
from categories.models import Category
from topics.serializers import TopicSerializer
from rest_framework import generics
from django.contrib.auth.models import User
# from topics.serializers import UserSerializer
from rest_framework import permissions
from topics.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'topics': reverse('topic-list', request=request, format=format),
    })

class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # def perform_create(self, serializer):
    # 	serializer.save(owner=self.request.user)
    def perform_create(self, serializer):
         serializer.save(category_id=self.request.data['category_id'])

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class TopicListByCategory(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the topics
        under the given category.
        """
        category_name = self.kwargs['category']
        category = Category.objects.filter(category_name=category_name)
        return Topic.objects.filter(category=category)

