from django.db import models

# Create your models here.
class sanpham(models.Model):
    idSP = models.IntegerField( primary_key="idSP")
    idLoaiSP = models.IntegerField()
    tenSP = models.CharField(max_length=100)
    DonGia = models.FloatField(default=0)
    GioiThieu = models.TextField()
    GiamGia  = models.IntegerField()
    image_link = models.CharField(max_length=100)
    image_list = models.TextField()
    timeNhap  =models.IntegerField(default=0)
    luotxem = models.IntegerField(default=0)
    SLTon = models.IntegerField()
    idtin = models.IntegerField()

