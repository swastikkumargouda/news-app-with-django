from django.urls import path
from .views import home, todays_news, trending

urlpatterns = [
    path('', home, name='home'),
    path('todays-news/', todays_news, name='todays_news'),
    path('trending/', trending, name='trending'),
]
