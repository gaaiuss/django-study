from django.contrib import admin

from blog.models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "id", "title", "short_description", "description"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "id", "name"
