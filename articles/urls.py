from django.contrib import admin
from django.urls import path
from articles import views

app_name = 'articles'

urlpatterns = [
    path('<article_id>', views.get_article, name='get_article'),
]