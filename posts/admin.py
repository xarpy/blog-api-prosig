from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from .models import BlogPost, Comment


class CommentCountFilter(SimpleListFilter):
    title = _("Number of comments")
    parameter_name = "comments_count"

    def lookups(self, request, model_admin):
        return [
            ("0", _("No comment")),
            ("1-5", _("1 to 5 comments")),
            ("6+", _("More than 5 comments")),
        ]

    def queryset(self, request, queryset):
        queryset = queryset.annotate(comment_count=Count("comments"))
        match self.value():
            case "0":
                return queryset.filter(comment_count=0)
            case "1-5":
                return queryset.filter(comment_count__gte=1, comment_count__lte=5)
            case "6+":
                return queryset.filter(comment_count__gt=5)
        return queryset


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "short_content", "comment_count")
    search_fields = ("title", "content")
    ordering = ("-id",)
    list_per_page = 20
    list_filter = (CommentCountFilter,)

    def queryset(self, request, queryset):
        return super().get_queryset(request).annotate(comment_count=Count("comments"))

    def short_content(self, obj):
        return (obj.content[:75] + "...") if len(obj.content) > 75 else obj.content

    short_content.short_description = "Content Preview"

    def comment_count(self, obj):
        return obj.comment_count

    comment_count.short_description = "Comments"


class KeywordContentFilter(SimpleListFilter):
    title = _("Contains keyword")
    parameter_name = "keyword"

    def lookups(self, request, model_admin):
        return [
            ("django", _("Django")),
            ("api", _("API")),
            ("bug", _("Bug")),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(content__icontains=self.value())
        return queryset


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "short_content", "created_at")
    search_fields = ("content", "post__title")
    list_filter = ("created_at", "post", KeywordContentFilter)
    ordering = ("-created_at",)
    autocomplete_fields = ("post",)
    list_per_page = 20

    def short_content(self, obj):
        return (obj.content[:50] + "...") if len(obj.content) > 50 else obj.content

    short_content.short_description = "Content Preview"
