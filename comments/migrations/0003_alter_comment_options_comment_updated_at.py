# Generated by Django 5.1.7 on 2025-03-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
