from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

user = get_user_model()

def validate_unique_title(value):
    """
    Валидатор для проверки уникальности названия поста.
    """
    if Article.objects.filter(title=value).exists():
        raise ValidationError(
            'Название не должно повторяться'
        )


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название',
        validators=[validate_unique_title]
    )
    author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self): 
        if len(self.text) > 140:
            return self.text[:140] + "..."
        else:
            return self.text

# Create your models here.