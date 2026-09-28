from django.contrib import admin

from blog.models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "id", "title", "short_description", "description"
    list_display_links = "id", "title"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"
