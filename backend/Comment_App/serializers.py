from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        user = Comment
        fields = ['id', 'user', 'video_id', 'text', 'likes', 'dislikes']
        depth = 1
