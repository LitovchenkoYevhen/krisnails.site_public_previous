# Generated by Django 3.2 on 2021-07-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20210703_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='master',
            name='surname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='master',
            name='telephone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер телефона без "+38"'),
        ),
    ]
