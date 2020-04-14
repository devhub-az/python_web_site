from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    fullName = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','fullName']

    def get_fullName(self,obj):
        return obj.get_full_name()


post_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'api:post-detail',
    lookup_field = 'pk'
)

class PostSerializer(serializers.ModelSerializer):
    detail_url = post_detail_url
    author = UserSerializer()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_count(self,obj):
        return obj.total_likes()

    def get_dislikes_count(self,obj):
        return obj.total_dislikes()


class PostCreateSerializer(serializers.ModelSerializer):
    detail_url = post_detail_url
    class Meta:
        model = Post
        fields = ['name','body','image','detail_url']