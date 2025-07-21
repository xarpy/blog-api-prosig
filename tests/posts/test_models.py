from posts.models import BlogPost, Comment


def test_blogpost_str():
    """Unit test to validate blogspot model"""
    post = BlogPost(title="Hello", content="World")
    assert str(post).endswith("+ - + Hello")


def test_comment_fields():
    """Unit test to validate comment models"""
    fields = [f.name for f in Comment._meta.fields]
    assert "content" in fields
    assert "post" in fields
