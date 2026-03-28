from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articleApp/article_list.html', {'page_obj': page_obj})
