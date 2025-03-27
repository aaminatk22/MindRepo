from django import forms
from .models import Article, Category

from django import forms
from .models import Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].required = False


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']