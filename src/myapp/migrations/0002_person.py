# Generated by Django 4.2.5 on 2023-09-10 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='メール')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='電話')),
                ('address', models.CharField(default='', max_length=255, verbose_name='住所')),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
