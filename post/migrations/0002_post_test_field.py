# Generated by Django 5.1.4 on 2024-12-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test_field',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
