from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Category
from .forms import ArticleForm
from comments.forms import CommentForm

from .forms import CategoryForm
from .models import Category


def article_list(request):
    category_id = request.GET.get('category')
    articles = Article.objects.all()
    categories = Category.objects.all()

    if category_id:
        articles = articles.filter(category_id=category_id)

    return render(request, 'articles/article_list.html', {
        'articles': articles,
        'categories': categories
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.views += 1
    article.save()
    comment_form = CommentForm()
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comment_form': comment_form
    })
@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = CategoryForm()
    return render(request, 'articles/category_form.html', {'form': form})
