# Converting objects into data types understandable by javascript and front-end frameworks

from rest_framework import serializers
from .models import Videos


class VideosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Videos
        fields = ['id', 
                  'video_id',
                  'video_title',
                  'description',
                  'publishing_datetime',
                  'thumbnail_url_s',
                  'thumbnail_url_m',
                  'thumbnail_url_h',
                  'channel_title', ]
