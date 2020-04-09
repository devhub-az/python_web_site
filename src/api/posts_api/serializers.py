from rest_framework import serializers
from blog.models import Post


post_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'api:post-detail',
    lookup_field = 'slug'
)

class PostSerializer(serializers.ModelSerializer):
    detail_url = post_detail_url
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    detail_url = post_detail_url
    class Meta:
        model = Post
        fields = ['name','body','image','detail_url']