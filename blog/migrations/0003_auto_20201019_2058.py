# Generated by Django 3.1.2 on 2020-10-19 20:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201019_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='subsribed',
            new_name='subscribed',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=datetime.datetime(2020, 10, 19, 20, 58, 28, 213338))),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]