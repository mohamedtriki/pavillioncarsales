# Generated by Django 3.2.5 on 2021-07-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20210719_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='slug',
            field=models.CharField(blank=True, help_text='required', max_length=200),
        ),
    ]
