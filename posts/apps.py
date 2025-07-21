from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Class to configure some options on the app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"
