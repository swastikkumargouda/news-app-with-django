import requests
from django.shortcuts import render
from django.conf import settings


API_KEY = '7d36363203ff4847820ed289d5883473'

def fetch_news(category):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    return articles

def home(request):
    trending_news = fetch_news('general')
    regular_news = fetch_news('business')  
    return render(request, 'news/home.html', {
        'trending_news': trending_news,
        'regular_news': regular_news
    })

def todays_news(request):
    todays_news = fetch_news('general')
    return render(request, 'news/todays_news.html', {'todays_news': todays_news})

def trending(request):
    trending_news = fetch_news('general')
    return render(request, 'news/trending.html', {'trending_news': trending_news})

