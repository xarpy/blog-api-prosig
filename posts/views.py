from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from posts.models import BlogPost
from posts.serializers import BlogPostDetailSerializer, BlogPostListSerializer, CommentSerializer


@extend_schema(
    summary="Create or list posts",
    responses={
        status.HTTP_200_OK: BlogPostListSerializer(many=True),
        status.HTTP_201_CREATED: BlogPostDetailSerializer,
    },
    request=BlogPostDetailSerializer,
    description="GET returns all posts with a number of comments. POST creates a new post.",
)
class BlogPostLisCreatetView(generics.ListCreateAPIView):
    """BlogPostLisCreatetView view class"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogPostDetailSerializer
        return super().get_serializer_class()


@extend_schema(
    summary="Post details",
    responses={status.HTTP_200_OK: BlogPostDetailSerializer, status.HTTP_404_NOT_FOUND: {"detail": "Post not found."}},
    description="Returns a specific post with its associated comments.",
)
class BlogPostRetrieveView(generics.RetrieveAPIView):
    """BlogPostRetrieveView view class"""

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    summary="Create a comment associate to post",
    request=CommentSerializer,
    responses={status.HTTP_201_CREATED: CommentSerializer, status.HTTP_404_NOT_FOUND: {"detail": "Post not found."}},
    description="Creates a new comment linked to the post ID provided.",
)
class CommentCreateView(generics.CreateAPIView):
    """CommentCreateView view class"""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["post_id"] = self.kwargs.get("pk")
        return context
