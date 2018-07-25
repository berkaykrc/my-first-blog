from django.db import models
from django.utils import timezone


class Categories(models.Model):
    ZARA = 'ZR'
    BERSHKA = 'BR'
    PULLBEAR = 'PB'
    HM = 'HM'
    STRADIVARIUS = 'STR'
    MANGO = 'MN'

    CATEGORY_CHOICES = (
        (ZARA, 'Zara'),
        (BERSHKA, 'Bershka'),
        (PULLBEAR, 'Pull&Bear'),
        (HM, 'H&M'),
        (STRADIVARIUS, 'Stradivarius'),
        (MANGO, 'Mango'),
    )

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Gonderi(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default='zara')
    yazari = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    baslik = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    yazi = models.TextField()
    olusturma_tarihi = models.DateTimeField(
        blank=True, null=True)


    def yayinla(self):
        self.olusturma_tarihi = timezone.now()
        self.save()

    def approved_comment(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.baslik




class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Gonderi', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
