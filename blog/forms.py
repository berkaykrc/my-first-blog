from django import forms
from .models import Gonderi, Comment, Categories


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name', 'slug',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Gonderi
        fields = ('baslik', 'yazi',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', )
