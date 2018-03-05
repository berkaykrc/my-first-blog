from django.db import models
from django.utils import timezone

class Gonderi(models.Model):
	yazari = models.ForeignKey('auth.User', on_delete=models.CASCADE)#başka bir modele referans tanımlar
	baslik = models.CharField(max_length=200)#belirli bir uzunlukta metin için tanımlanır
	yazi = models.TextField()#uzunluğu belli olmayan bir metin uzunluğu için tanımlanır
	olusturma_tarihi = models.DateTimeField(blank=True, null=True)#gün ay yıl bilgisi için tanımlandı
	
	def yayinla(self):
		self.olusturma_tarihi = timezone.now()
		self.save()
	
	def __str__(self):
		return self.baslik