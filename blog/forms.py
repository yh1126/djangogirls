from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date',)
        # TODO このままだとpublished_dateの入力エリアがテキストの
        # 入力の仕方になっているのでdatetime型で強制的に入力できるようにする
