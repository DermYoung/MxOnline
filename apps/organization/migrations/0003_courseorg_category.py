# Generated by Django 2.2.7 on 2019-11-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20191110_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
    ]
