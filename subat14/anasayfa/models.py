from django.db import models

# Create your models here.
class ogr(models.Model):
    isim = models.CharField(max_length=50)
    def __str__(self):
        return self.isim

class bilgi(models.Model):
    kategori =  models.ForeignKey(
        ogr, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=100, null=True)
    aciklama = models.TextField(max_length=250, null=True)
    resim = models.FileField(upload_to='kisiresmi/',blank= True,null = True,verbose_name="kisi resmi ekleyin")
    def __str__(self):
        return self.isim
        