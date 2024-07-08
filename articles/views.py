from .models import Article
from django.shortcuts import render
from django.http import Http404
from .models import user
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from .models import Article
from django.urls import reverse_lazy
from django.utils import timezone




def archive(request):
    posts = Article.objects.all()
    context = {'posts': posts}
    return render(request, 'archive.html', context)


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
    
from django.urls import reverse_lazy

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'text', 'author']
    template_name = 'create_post.html'

    def get_success_url(self):
        return reverse_lazy('articles:get_article', args=[str(self.object.id)])

    

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
            'text': request.POST["text"],
            'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
            # если поля заполнены без ошибок
                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('articles:get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

 
