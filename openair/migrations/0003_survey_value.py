# Generated by Django 2.0.5 on 2018-05-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openair', '0002_auto_20180523_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='value',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
