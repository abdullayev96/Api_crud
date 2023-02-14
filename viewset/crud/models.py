from django.db import models

class Customer(models.Model):

    STATUS_PLACE   = [('uzbekistan', 'Uzbekistan'),
                      ('rossiya', "Rossiya"), ('turkiya', "Tukiya"), ('saudiya', "Saudiya"),
                      ('xitoy', "Xitoy"), ('germaniya', "Germaniya"),
                      ('usa', "Usa"), ('yaponiya', "Japon")]

    name  = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images')
    price = models.IntegerField()
    number = models.CharField(max_length=200)
    place  = models.CharField(max_length=20, choices=STATUS_PLACE, default='tashkent')
    is_published = models.BooleanField(default=True)
    category  = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name