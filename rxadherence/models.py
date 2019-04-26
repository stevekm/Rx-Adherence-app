from django.db import models

# Create your models here.
class Drug(models.Model):
    """
    A test model to make sure the database workse
    """
    name = models.CharField(unique = True, max_length=255)
    imported = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.name)[0:10])

class User(models.Model):
    """
    A test model to make sure the database workse
    """
    username = models.CharField(unique = True, max_length=255)
    imported = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.username)[0:10])

# class Usage()
