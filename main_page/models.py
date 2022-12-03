from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Advantages(models.Model):
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Instructions(models.Model):
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Success(models.Model):
    image = models.ImageField(upload_to='')
    description = models.TextField()

class Instruction1(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Course(models.Model):
    image = models.ImageField(upload_to='')
    category = models.CharField(max_length=10)
    description = models.TextField()
    price = models.PositiveIntegerField()
    weeks = models.PositiveIntegerField()
    practical = models.PositiveIntegerField()

    def __str__(self):
        return self.category