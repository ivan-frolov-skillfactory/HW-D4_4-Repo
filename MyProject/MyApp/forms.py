from django.forms import ModelForm, BooleanField
from .models import Post


# создаём модельную форму
class PostForm(ModelForm):


    class Meta:
        model = Post  # это модель, по которой будет строиться форма

        # поля, которые будут выводиться на страничке
        fields = ['author', 'header', 'body', 'post_date']



