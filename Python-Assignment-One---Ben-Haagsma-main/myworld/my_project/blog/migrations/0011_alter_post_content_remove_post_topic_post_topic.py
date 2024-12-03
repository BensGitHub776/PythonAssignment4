# Generated by Django 5.1.1 on 2024-10-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ManyToManyField(null=True, related_name='topics', to='blog.topic'),
        ),
    ]