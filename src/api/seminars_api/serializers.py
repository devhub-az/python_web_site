from rest_framework import serializers
from seminars.models import Seminar


seminar_detail_url = serializers.HyperlinkedIdentityField(
    view_name = 'api:seminar-detail',
    lookup_field = 'pk'
)


class SeminarSerializer(serializers.ModelSerializer):
    detail_url = seminar_detail_url
    class Meta:
        model = Seminar
        fields = '__all__'


class SeminarCreateSerializer(serializers.ModelSerializer):
    detail_url = seminar_detail_url
    class Meta:
        model = Seminar
        fields = ['id','title','content','detail_url','seminar_photo','seminar_place','seminar_date',]