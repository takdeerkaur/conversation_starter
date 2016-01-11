from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'topics': reverse('topic-list', request=request, format=format),
    })

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # def perform_create(self, serializer):
    # 	serializer.save(owner=self.request.user)



class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


