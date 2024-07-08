# Импортируем ошибку валидации.
from django.core.exceptions import ValidationError
from .models import Article


# На вход функция будет принимать дату рождения.
# Функция не должна ничего возвращать.
def validate_unique_title(value):
    """
    Валидатор для проверки уникальности названия поста.
    """
    if Article.objects.filter(title=value).exists():
        raise ValidationError(
            'Название не должно повторяться'
        )