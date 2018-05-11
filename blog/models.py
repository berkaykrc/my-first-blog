from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
    yazari = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    olusturma_tarihi = models.DateTimeField(
        blank=True, null=True)

    def yayinla(self):
        self.olusturma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
