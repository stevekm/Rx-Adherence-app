from django.db import models

# Create your models here.
class Drug(models.Model):
    """
    A test model to make sure the database workse
    """
    name = models.CharField(max_length=255)
    imported = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.name)[0:10])
