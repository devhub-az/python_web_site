from rest_framework import serializers
from comments.models import Comment
from ..posts_api.serializers import PostSerializer
from django.contrib.auth.models import User


comment_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'api:comment-detail',
    lookup_field =  'pk',
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email']

class CommentSerializer(serializers.ModelSerializer):
    detail_url = comment_detail_url
    post = PostSerializer(many=False , read_only=False)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    detail_url = comment_detail_url
    class Meta:
        model = Comment
        fields = ['post','user','body','created_on','parent','detail_url']
    