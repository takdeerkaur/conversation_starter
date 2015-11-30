from topics.models import Topic
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



class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

# TODO: Make the following lists by category sort dynamically, if possible. Does there really need to be a 
# new view class / url for each different category?
class EntertainmentTopicList(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the topics
        under the Entertainment category.
        """
        return Topic.objects.filter(category='ENT')

class SportsTopicList(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the topics
        under the Sports category.
        """
        return Topic.objects.filter(category='SPO')

class ArtsTopicList(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the topics
        under the Arts category.
        """
        return Topic.objects.filter(category='ART')

