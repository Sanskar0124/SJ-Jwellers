# Generated by Django 3.1.7 on 2021-04-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210408_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]