# Generated by Django 4.0.3 on 2022-04-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Science', 'Science'), ('Culture', 'Culture'), ('Movie', 'Movie')], default='', max_length=30),
        ),
    ]
