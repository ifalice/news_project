from django.contrib import admin
from .models import News


class FilterRatingNews(admin.SimpleListFilter):
    title = 'Rating News'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'bad news'),
            ('41 to 60', 'normal news'),
            ('61 to 80', 'good news'),
            ('>81', 'great news'),
            
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lte = 40)
        elif self.value() == '41 to 60':
            return queryset.filter(rating__gte = 41).filter(rating__lte = 60)
        elif self.value() == '61 to 80':
            return queryset.filter(rating__gte = 61).filter(rating__lte = 80)
        elif self.value() == '>81':
            return queryset.filter(rating__gte = 81)
        return queryset

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','rating','rating_news']
    list_editable = ['category','rating']
    ordering = ['category',]
    actions = ['set_culture_category', 'set_sport_category']
    search_fields = ['title', 'category']
    list_filter = ['category', FilterRatingNews]

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

    @admin.action()
    def set_sport_category(self, request, queryset):
        Sport = 'Sport'
        queryset.update(category = News.Sport)

admin.site.register(News, NewsAdmin)