from django.db import models

# Create your models here.
class Members(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    Dbirthday = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    Pbirthday = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    poids = models.CharField(max_length=50)
    Ssante = models.CharField(max_length=200)
    job = models.CharField(max_length=50)
    cancerType = models.CharField(max_length=50)
    DateDiag = models.CharField(max_length=50)
    medcinNote = models.CharField(max_length=9000)
    MdeFam = models.CharField(max_length=50)
    NumMdeFam = models.CharField(max_length=50)
    Sfin = models.CharField(max_length=50)
    etatCivil = models.CharField(max_length=50)
    def __str__(self):
        return self.fname + " " + self.lname