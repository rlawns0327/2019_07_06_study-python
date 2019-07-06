from django.contrib import admin
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['updatded_at']
    search_fields = ['title']