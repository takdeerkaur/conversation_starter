from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


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

class CategoryIdByNameList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_queryset(self):
        """
        This view should return a list of all the topics
        under the given category.
        """
        category = self.kwargs['category']
        # TODO: implement 404 if no category exists
        # try:
        #     Category.objects.filter(category_name=category)
        # except ObjectDoesNotExist:
        #     raise Http404("Category does not exist")
        return Category.objects.filter(category_name=category)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


