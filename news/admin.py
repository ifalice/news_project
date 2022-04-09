from django.contrib import admin
from .models import News



class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','rating','rating_news']
    list_editable = ['category','rating']
    ordering = ['category',]
    actions = ['set_culture_category']

    def rating_news(self, news):
        if news.rating < 50:
            return 'Bad News'
        elif news.rating <75:
            return 'Good News'
        return 'Great News'

    @admin.action()
    def set_culture_category(self, request, queryset):
        Culture = 'Culture'
        queryset.update(category = News.CULTURE)

admin.site.register(News, NewsAdmin)