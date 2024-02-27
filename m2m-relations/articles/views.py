from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    article_list = Article.objects.prefetch_related('tags')
    context = {'object_list': article_list, }

    return render(request, template, context)
