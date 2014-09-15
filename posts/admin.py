from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
	model = Comment
	extra = 3

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=('user','text','date')
	inlines= [CommentInline]