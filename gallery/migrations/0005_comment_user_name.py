# Generated by Django 4.2 on 2024-10-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_name',
            field=models.CharField(default='Anonymous', max_length=40),
        ),
    ]
