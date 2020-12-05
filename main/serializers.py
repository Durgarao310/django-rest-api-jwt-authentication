from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['user',]
    def create(self, validated_data):
        data = validated_data.copy()
        data['user'] = self.context['request'].user

        return super(PostSerializer, self).create(data)