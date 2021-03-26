# Generated by Django 3.1.7 on 2021-03-26 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(default='123456789', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
