import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken, Token

from posts.models import BlogPost


@pytest.fixture
def api_client():
    """Function repsonsible to generate a api client fixture instance.
    Returns:
        mock: Return a mock of api client instance.
    """
    return APIClient()


@pytest.fixture
def create_user(db):
    """Function responsible to generate a user fixture for tests.
    Args:
        db (mock): Receives a database mock from pytest.
    Returns:
        user: Returns a user instance
    """
    user = User.objects.create_user(
        username="testuser",
        email="test@test.com",
        password="12345",
        is_staff=True,
    )
    return user


@pytest.fixture
def auth_client(api_client, create_user):
    """Function repsonsible to create a fixture for client authenticated
    Args:
        api_client (object): Receives the api client fixture
        create_user (object): Receives the user fixture

    Returns:
        client: Return a api client authenticated
    """
    refresh = RefreshToken.for_user(create_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {str(refresh.access_token)}")
    return api_client


@pytest.fixture
def create_post(db):
    """Function responsible to create post fixture.
    Args:
        db (mock): Receives a database mock from pytest.
    """

    def _create_post(title="Sample title", content="Sample content"):
        return BlogPost.objects.create(title=title, content=content)

    return _create_post


@pytest.fixture(scope="function")
def create_token(create_user) -> Token:
    """Fixture to provide an Token, based on user instance
    Args:
        create_user (function): Received the fixture function to create a user instance
    Returns:
        str: Return a access token
    """
    user = create_user
    refresh = RefreshToken.for_user(user)
    return refresh
