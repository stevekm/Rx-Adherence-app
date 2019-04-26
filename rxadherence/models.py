from django.db import models

# Create your models here.
class Drug(models.Model):
    """
    Model of drugs to be used in the app
    """
    name = models.CharField(unique = True, max_length=255)
    imported = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.name)[0:10])

class User(models.Model):
    """
    Users in the app
    """
    username = models.CharField(unique = True, max_length=255)
    imported = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return(str(self.username)[0:10])

class Usage(models.Model):
    """
    Logging of when a user takes a drug
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        label = "{0}:{1} [{2}]".format(self.username.username, self.drug.name[0:6], self.time)
        return(label)
