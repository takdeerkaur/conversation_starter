from rest_framework import serializers
from topics.models import Topic
# from django.contrib.auth.models import User

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Topic
        fields = ('topic_name',)


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

#     class Meta:
#         model = User
#         fields = ('url', 'username', 'snippets')