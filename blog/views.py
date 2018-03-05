from django.shortcuts import render, get_object_or_404
from .models import Gonderi
from django.utils import timezone


def post_list(request):
	gonderiler = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('olusturma_tarihi')
	return render(request, 'blog/post_list.html', {'gonderiler': gonderiler})
def post_detail(request, pk):
	post = get_object_or_404(Gonderi, pk=pk)
	return render(request, 'blog/post_details.html', {'gonderi': post})