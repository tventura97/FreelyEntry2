# Generated by Django 2.1.5 on 2019-01-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20190124_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='number',
            field=models.CharField(default=1234567890, max_length=15),
            preserve_default=False,
        ),
    ]