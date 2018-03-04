from django.shortcuts import render
from .models import Gonderi
from django.utils import timezone


def post_list(request):
	gonderiler = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('olusturma_tarihi')
	return render(request, 'blog/post_list.html', {'gonderiler': gonderiler})