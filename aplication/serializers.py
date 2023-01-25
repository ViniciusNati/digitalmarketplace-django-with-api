from rest_framework import serializers
from .models import Post,Category,Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'cat',
            'image',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
        'user',
        'id',
        'title',
        'cat',
        'price',
        'add_date',
        'slug',
        'published',
        'premium',
        'amount',
        'description',
        'image',
        'amountselled',
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
        'user',
        'post',
        'body',
        'created_at',
        'published',
        ]
