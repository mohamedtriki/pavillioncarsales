# Generated by Django 3.2.5 on 2021-07-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_vehicle_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image_10',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_11',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_12',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_13',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_14',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_15',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_16',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_17',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_18',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_19',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_2',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_20',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_21',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_22',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_23',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_24',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_25',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_26',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_27',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_28',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_29',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_3',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_30',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_31',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_32',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_33',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_34',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_35',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_36',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_4',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_5',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_6',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_7',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_8',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image_9',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='slug',
            field=models.SlugField(help_text='required', max_length=200),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='thumb_image',
            field=models.ImageField(blank=True, help_text='optional', upload_to='img/img'),
        ),
    ]
