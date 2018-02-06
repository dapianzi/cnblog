from django import forms

from app.models import Article


class ArticleForm(forms.ModelForm):
    def is_valid(self):
        return True

    class Meta:
        model = Article
        exclude = ['pub_time']


# todo 评论的表单