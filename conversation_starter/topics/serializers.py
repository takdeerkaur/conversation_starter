from rest_framework import serializers
from categories.serializers import CategorySerializer
from topics.models import Topic
# from django.contrib.auth.models import User

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Topic
        fields = ('topic_name', 'category', 'category_id')
        read_only_fields = ('category_id',)


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

#     class Meta:
#         model = User
#         fields = ('url', 'username', 'snippets')