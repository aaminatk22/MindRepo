from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from articles.models import Article
from .models import Comment
from .forms import CommentForm

@login_required
def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
    return redirect('articles:article_detail', pk=article_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    article_id = comment.article.id
    if request.user == comment.author:
        comment.delete()
    return redirect('articles:article_detail', pk=article_id)