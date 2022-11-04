from django.db import models

from apps.category.models import Category


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    info = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to='rooms/image1/')
    image2 = models.ImageField(upload_to='rooms/image2/')
    image3 = models.ImageField(upload_to='rooms/image3/')
    image4 = models.ImageField(upload_to='rooms/image4/')
    floor = models.IntegerField(default=1)
    room_number = models.CharField(max_length=10)
    bedroom = models.IntegerField(default=0)
    hall = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    single_beds = models.IntegerField(default=0)
    double_beds = models.IntegerField(default=0)
    air_conditioner = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    hair_dryer = models.BooleanField(default=False)
    iron = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    TV = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'
        ordering = ['name']
