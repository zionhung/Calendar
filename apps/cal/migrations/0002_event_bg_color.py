# Generated by Django 2.2.7 on 2019-11-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='bg_color',
            field=models.CharField(default='#000000', max_length=20),
            preserve_default=False,
        ),
    ]