from django.db import models


class Header(models.Model):
    logo = models.ImageField(upload_to="Logo/")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()


class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='Clinic Service/')


class Region(models.Model):
    name = models.CharField(max_length=255)


class Photo(models.Model):
    image = models.ImageField(upload_to='Clinic/')


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    photo = models.ManyToManyField(Photo)
    address = models.CharField(max_length=255)
    number = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    rating = models.IntegerField()
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    rating = models.IntegerField()
    price = models.IntegerField()
    experience = models.IntegerField()
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
