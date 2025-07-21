import uuid

from django.db import models


class BlogPost(models.Model):
    """BlogPost Model class"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False, help_text="")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "BlogPost"
        verbose_name_plural = "BlogPosts"
        db_table = "posts"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.id} + - + {self.title}"


class Comment(models.Model):
    """Comment Model class"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comment"
        ordering = ["-created_at"]
