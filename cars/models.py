from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class feature(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name 


class make(models.Model):
    makes=(('Alfa Romeo ','Alfa Romeo'),('Audi ','Audi'),('bmw','bmw'),('Citroen','Citroen'),('Dacia ','Dacia'),('Fiat ','Fiat'),('Ford','Ford'),('Honda','Honda'),('Hyundai','Hyundai'),('Jaguar ','Jaguar'),('Jeep','Jeep'),('Kia','Kia'),('Land Rover ','Land Rover'),('Mazda','Mazda'),('Mercedes','Mercedes'),('Mitsubishi ','Mitsubishi'),('Nissan ','Nissan'),('Peugeot','Peugeot'),('Porsche','Porsche'),('Renault','Renault'),('Skoda ','Skoda'),('Suzuki','Suzuki'),('Toyota','Toyota'),('Vauxhall ','Vauxhall'),('Volkswagen','Volkswagen'),('Volvo','Volvo'))
    make=models.CharField(max_length=100,help_text = "optional",choices=makes,blank=True)
    def __str__(self):
        return self.make

class model(models.Model):
    make = models.ForeignKey(make,on_delete=models.CASCADE)
    model = models.CharField(max_length=100,help_text = "optional",blank=True)

    def __str__(self):
        return self.model




class vehicle(models.Model):
    transmission=(("Manual","Manual"),("Automatic","Automatic"),("Semi-automatic","Semi-automatic"),("CVT","CVT"))
    fuel=(("Petrol","Petrol"),("Diesel","Diesel"),("Hybrid","Hybrid"),("Electric","Electric"),("LPG","LPG"))
    title= models.CharField(max_length=200,help_text = "optional")
    slug= models.SlugField(max_length=200,help_text = "required",blank=False)
    title_description=models.CharField(max_length=350)
    price=models.FloatField(help_text = "use . not ,",blank=False)
    make=models.ForeignKey(make,on_delete=models.CASCADE)
    model=models.ForeignKey(model,on_delete=models.CASCADE)
    mileage=models.FloatField(help_text = "use . not ,",blank=False,default=45)
    MPG=models.CharField(max_length=100,help_text = "optional",blank=False)
    colour=models.CharField(max_length=100,blank=True)
    transmission=models.CharField(max_length=200,choices=transmission)
    fuel_type =models.CharField(max_length=100,blank=True,choices=fuel)
    body_style=models.CharField(max_length=100,blank=True)
    first_registration_date=models.CharField(max_length=100,help_text = "separate by /",blank=True)
    engine_size=models.CharField(max_length=100,blank=True)
    vehicle_location=models.CharField(max_length=100 ,blank=True,default='Pavillion Car Sales',help_text = "default is Pavillion Car Sales")
    feature=models.ManyToManyField(feature)
    youtube_link=models.CharField(max_length=600,help_text = "pste video link",blank=True)
    thumb_image= models.ImageField(blank=True ,help_text="optional")
    image_2= models.ImageField(blank=True ,help_text="optional")
    image_3= models.ImageField(blank=True ,help_text="optional")
    image_4= models.ImageField(blank=True ,help_text="optional")
    image_5= models.ImageField(blank=True ,help_text="optional")
    image_6= models.ImageField(blank=True ,help_text="optional")
    image_7= models.ImageField(blank=True ,help_text="optional")
    image_8= models.ImageField(blank=True ,help_text="optional")
    image_9= models.ImageField(blank=True ,help_text="optional")
    image_10= models.ImageField(blank=True ,help_text="optional")
    image_11= models.ImageField(blank=True ,help_text="optional")
    image_12= models.ImageField(blank=True ,help_text="optional")
    image_13= models.ImageField(blank=True ,help_text="optional")
    image_14= models.ImageField(blank=True ,help_text="optional")
    image_15= models.ImageField(blank=True ,help_text="optional")
    image_16= models.ImageField(blank=True ,help_text="optional")
    image_17= models.ImageField(blank=True ,help_text="optional")
    image_18= models.ImageField(blank=True ,help_text="optional")
    image_19= models.ImageField(blank=True ,help_text="optional")
    image_20= models.ImageField(blank=True ,help_text="optional")
    image_21= models.ImageField(blank=True ,help_text="optional")
    image_22= models.ImageField(blank=True ,help_text="optional")
    image_23= models.ImageField(blank=True ,help_text="optional")
    image_24= models.ImageField(blank=True ,help_text="optional")
    image_25= models.ImageField(blank=True ,help_text="optional")
    image_26= models.ImageField(blank=True ,help_text="optional")
    image_27= models.ImageField(blank=True ,help_text="optional")
    image_28= models.ImageField(blank=True ,help_text="optional")
    image_29= models.ImageField(blank=True ,help_text="optional")
    image_30= models.ImageField(blank=True ,help_text="optional")
    image_31= models.ImageField(blank=True ,help_text="optional")
    image_32= models.ImageField(blank=True ,help_text="optional")
    image_33= models.ImageField(blank=True ,help_text="optional")
    image_34= models.ImageField(blank=True ,help_text="optional")
    image_35= models.ImageField(blank=True ,help_text="optional")
    image_36= models.ImageField(blank=True ,help_text="optional")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title 




class contact(models.Model):
    name= models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=300,blank=True)
    email=models.EmailField("Email address",blank=True)
    message=models.TextField(blank=True)
    def __str__(self):
        return self.name 