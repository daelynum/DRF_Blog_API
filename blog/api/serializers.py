from rest_framework import serializers

from .models import Post, Comment


class APIPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'header', 'content')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class APICommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'parent')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
