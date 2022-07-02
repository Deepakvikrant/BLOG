from sqlite3 import Timestamp
from django.db import models

# Create your models here.
# this is database ====exel workbook
#models in django ===table exel sheet 

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank= True)

    def __str__(self):
        return "MESSAGGE FROM :- " + self.name + "  Email:-  " + self.email



