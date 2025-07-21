from rest_framework import serializers
from rest_framework.exceptions import NotFound

from posts.models import BlogPost, Comment


class CommentSerializer(serializers.ModelSerializer):
    """CommentSerializer serializer class"""

    class Meta:
        model = Comment
        fields = ["id", "content", "created_at"]

    def create(self, validated_data):
        post_id = self.context.get("post_id")
        try:
            post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            raise NotFound("Post not found.")

        return Comment.objects.create(post=post, **validated_data)


class BlogPostListSerializer(serializers.ModelSerializer):
    """BlogPostListSerializer serializer class"""

    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = BlogPost
        fields = ["id", "title", "comments_count"]


class BlogPostDetailSerializer(serializers.ModelSerializer):
    """BlogPostDetailSerializer serializer class"""

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "comments"]
