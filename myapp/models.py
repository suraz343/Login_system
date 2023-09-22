from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name + "- "+ self.email