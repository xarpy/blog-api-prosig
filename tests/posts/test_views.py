import uuid

import pytest
from django.urls import reverse

from posts.models import Comment


@pytest.mark.django_db
def test_list_blog_posts(auth_client, create_post):
    """Unit test to list a blog post itens"""
    create_post()
    url = reverse("post-list-create")
    response = auth_client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.django_db
def test_create_blog_post(auth_client):
    """Unit test for create a blog post"""
    url = reverse("post-list-create")
    payload = {"title": "Test Post", "content": "This is the body"}
    response = auth_client.post(url, data=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Post"


@pytest.mark.django_db
def test_retrieve_blog_post(auth_client, create_post):
    """Unit test to get the blog post"""
    post = create_post()
    url = reverse("post-detail", kwargs={"pk": post.id})
    response = auth_client.get(url)
    assert response.status_code == 200
    assert response.json()["id"] == str(post.id)


@pytest.mark.django_db
def test_create_comment_success(auth_client, create_post):
    """Unit test for create success comment"""
    post = create_post()
    url = reverse("post-comment-create", kwargs={"pk": post.id})
    payload = {"content": "Nice post!"}
    response = auth_client.post(url, data=payload)
    assert response.status_code == 201
    assert Comment.objects.filter(post=post).count() == 1


@pytest.mark.django_db
def test_create_comment_invalid_post(auth_client):
    """Unit test for create invalid commment"""
    url = reverse("post-comment-create", kwargs={"pk": uuid.uuid4()})
    response = auth_client.post(url, data={"content": "Invalid post"})
    assert response.status_code == 404
