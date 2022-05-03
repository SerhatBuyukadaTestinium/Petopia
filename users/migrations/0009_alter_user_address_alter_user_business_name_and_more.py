# Generated by Django 4.0.4 on 2022-05-03 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_pet_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='information',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]