# Generated by Django 3.2.5 on 2021-07-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210716_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.CharField(blank=True, help_text='optional', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='MPG',
            field=models.CharField(help_text='optional', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.FloatField(help_text='use . not ,'),
        ),
    ]
