# Generated by Django 3.2.5 on 2021-07-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='optional', max_length=200)),
                ('title_description', models.CharField(max_length=350)),
                ('price', models.FloatField(blank=True, help_text='use . not ,')),
                ('make', models.CharField(choices=[('Alfa Romeo ', 'Alfa Romeo'), ('Audi ', 'Audi'), ('bmw', 'bmw'), ('Citroen', 'Citroen'), ('Dacia ', 'Dacia'), ('Fiat ', 'Fiat'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Jaguar ', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Land Rover ', 'Land Rover'), ('Mazda', 'Mazda'), ('Mercedes', 'Mercedes'), ('Mitsubishi ', 'Mitsubishi'), ('Nissan ', 'Nissan'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Skoda ', 'Skoda'), ('Suzuki', 'Suzuki'), ('Toyota', 'Toyota'), ('Vauxhall ', 'Vauxhall'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], help_text='optional', max_length=100)),
                ('mileage', models.FloatField(default=45, help_text='use . not ,')),
                ('MPG', models.CharField(blank=True, help_text='optional', max_length=100)),
                ('colour', models.CharField(blank=True, max_length=100)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Semi-automatic', 'Semi-automatic'), ('CVT', 'CVT')], max_length=200)),
                ('fuel_type', models.CharField(blank=True, max_length=100)),
                ('body_style', models.CharField(blank=True, max_length=100)),
                ('first_registration_date', models.CharField(blank=True, help_text='separate by /', max_length=100)),
                ('engine_size', models.CharField(blank=True, max_length=100)),
                ('vehicle_location', models.CharField(blank=True, default='Pavillion Car Sales', help_text='default is Pavillion Car Sales', max_length=100)),
                ('youtube_link', models.CharField(blank=True, help_text='pste video link', max_length=600)),
                ('thumb_image', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_2', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_3', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_4', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_5', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_6', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_7', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_8', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_9', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_10', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_11', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_12', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_13', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_14', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_15', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_16', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_17', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_18', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_19', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_20', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_21', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_22', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_23', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_24', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_25', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_26', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_27', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_28', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_29', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_30', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_31', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_32', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_33', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_34', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_35', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('image_36', models.FileField(blank=True, help_text='optional', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('feature', models.ManyToManyField(to='cars.feature')),
            ],
        ),
    ]
