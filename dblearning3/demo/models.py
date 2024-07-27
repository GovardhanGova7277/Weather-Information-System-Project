from django.db import models

# Create your models here.

class Weather(models.Model):
    cityName = models.CharField(max_length = 100, unique = True)
    temperature = models.FloatField(null = False)
    pressure = models.FloatField(null = False)
    rainPossibility = models.BooleanField(default = False)
    amountOfRain = models.IntegerField(default = 0)
    description = models.TextField()
    images = models.FileField(upload_to= 'static/uploads/', null = True)
    image_path = models.CharField(max_length = 1000, default = '/uploads/empty.jpg')

    def __str__(self):
        return f'Weather Info About: {self.cityName}'



class Author(models.Model):
    a_name = models.CharField(max_length = 100, unique = True, null = False)
    a_age = models.IntegerField(null = False)   
    a_email=models.CharField(max_length=30,null=False)

    def __str__(self):
        return f'{self.a_name} --> {self.a_age}'
    


    


class Book(models.Model):
    isbn = models.CharField(max_length = 100, unique = True, null = False)
    b_name = models.CharField(max_length = 100, unique = True, null = False)
    author_info = models.ForeignKey(Author,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.isbn} --> {self.b_name} --> {self.author_info}'
    




