# Generated by Django 3.2 on 2021-07-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20210703_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Сертификат')),
                ('data', models.CharField(blank=True, max_length=80, verbose_name='Когда выдан')),
                ('school', models.CharField(blank=True, max_length=80, verbose_name='Школа маникюра')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.DeleteModel(
            name='Diplom',
        ),
    ]
