# Generated by Django 2.2.12 on 2022-03-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20220325_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='零售价'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=100, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=1, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=11, unique=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='书名'),
        ),
    ]
