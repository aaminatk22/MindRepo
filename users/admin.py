from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from .models import Profile
from articles.models import Article, Category  # Import your models
from comments.models import Comment  # Import your models


class CustomAdminSite(AdminSite):
    site_header = 'Blog Administration'
    site_title = 'Blog Admin Portal'
    index_title = 'Welcome to Blog Admin'

    def login(self, request, extra_context=None):
        try:
            return super().login(request, extra_context)
        except Exception as e:
            if "has no profile" in str(e):
                User = get_user_model()
                user = request.user
                if user.is_authenticated and not hasattr(user, 'profile'):
                    Profile.objects.get_or_create(user=user)
                return super().login(request, extra_context)
            raise


# Instantiate the custom admin site
admin_site = CustomAdminSite(name='custom_admin')

# Register User model
User = get_user_model()


@admin.register(User, site=admin_site)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')


# Register Profile model
@admin.register(Profile, site=admin_site)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio_short')
    search_fields = ('user__username', 'bio')

    def bio_short(self, obj):
        return obj.bio[:50] + '...' if len(obj.bio) > 50 else obj.bio

    bio_short.short_description = 'Bio Excerpt'


# Register Article model
@admin.register(Article, site=admin_site)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('category', 'created_at', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)


# Register Category model
@admin.register(Category, site=admin_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')
    search_fields = ('name',)

    def article_count(self, obj):
        return obj.article_set.count()

    article_count.short_description = 'Articles'


# Register Comment model
@admin.register(Comment, site=admin_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_at', 'content_short')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')

    def content_short(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    content_short.short_description = 'Comment'