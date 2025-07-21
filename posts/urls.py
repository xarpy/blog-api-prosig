from django.urls import path

from posts.views import BlogPostLisCreatetView, BlogPostRetrieveView, CommentCreateView

urlpatterns = [
    path("posts", BlogPostLisCreatetView.as_view(), name="post-list-create"),
    path("posts/<uuid:pk>", BlogPostRetrieveView.as_view(), name="post-detail"),
    path("posts/<uuid:pk>/comments", CommentCreateView.as_view(), name="post-comment-create"),
]
