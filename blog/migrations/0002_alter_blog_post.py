# Generated by Django 4.0.4 on 2022-05-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(max_length=2500, null=True),
        ),
    ]