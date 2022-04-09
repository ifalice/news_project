from django.shortcuts import render
from django.http import HttpResponse
from .models import News



def main_menu(request):
    all_news = News.objects.all()
    context = {
        'all_news':all_news,
    }
    return render(request, 'news/main_menu.html', context = context)

def show_category(request):
    categorys = ['movie', 'culture', 'sport', 'science']
    return render(request, 'news/show_category.html', context = {'categorys':categorys})    

def show_news_by_category(request, name_category):
    news_by_category = News.objects.filter(category=f'{name_category.title()}')
    context = {
        'news_by_category':news_by_category,
        'name_category':name_category
    }
    return render(request, 'news/show_news_by_category.html', context=context)

    