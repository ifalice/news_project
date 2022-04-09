from django.db import models

class News(models.Model):
    CULTURE = 'Culture'

    CATEGORY_CHOISES = [
        ('Sport', 'Sport'),
        ('Science', 'Science'),
        ('Culture', 'Culture'),
        ('Movie', 'Movie'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOISES, default='')
    content_news = models.TextField()
    rating = models.IntegerField(default=60)

    def __str__(self):
        return f'{self.title} - {self.category} - {self.content_news}'
