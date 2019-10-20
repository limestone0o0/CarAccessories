from rest_framework import serializers
from .models import CarnewsCarnews


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarnewsCarnews
        fields = [
            'news_title', 'news_time_str', 'news_art_time', 'news_list_img',
            'news_path', 'news_read_num', 'news_comment_num', 'news_abstract',
            'news_art_img', 'news_art_content','id'
            ]

