from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name = 'main_menu'),
    path('category/', views.show_category, name = 'category'),
    path('category/<str:name_category>', views.show_news_by_category, name = 'show_news_by_category')
]