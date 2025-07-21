import pytest

from posts.serializers import BlogPostDetailSerializer, CommentSerializer


@pytest.mark.django_db
def test_blogpost_detail_serializer_output(create_post):
    """Unit test to validate blogpost detail serializer"""
    post = create_post()
    serializer = BlogPostDetailSerializer(post)
    data = serializer.data
    assert "id" in data
    assert "comments" in data
    assert data["title"] == post.title


@pytest.mark.django_db
def test_comment_serializer_create(create_post):
    """Unit test for comment serializer"""
    post = create_post()
    serializer = CommentSerializer(data={"content": "Great"}, context={"post_id": post.id})
    assert serializer.is_valid()
    instance = serializer.save()
    assert instance.post == post
