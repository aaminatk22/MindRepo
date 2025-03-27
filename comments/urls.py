from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('article/<int:article_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]