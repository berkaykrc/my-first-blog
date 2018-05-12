from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Gonderi
from django.db.models import Q
from django.utils import timezone
from .forms import PostForm


def post_list(request):
    gonderiler = Gonderi.objects.filter(
        olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi')
    return render(request, 'blog/post_list.html', {'gonderiler': gonderiler})


def post_detail(request, pk):
    post = get_object_or_404(Gonderi, pk=pk)
    return render(request, 'blog/post_detail.html', {'gonderi': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazari = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Gonderi, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.yazari = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Gonderi.objects.filter(olusturma_tarihi__isnull=True).\
        order_by('olusturma_tarihi')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Gonderi, pk=pk)
    post.yayinla()
    return redirect('post_detail', pk=pk)


def post_remove(request, pk):
    post = get_object_or_404(Gonderi, pk=pk)
    post.delete()
    return redirect('post_list')


def zara(request):
    zara_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi')\
        .filter(Q(baslik__contains='Zara') | Q(baslik__contains='zara'))
    zara_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Zara_Logo.svg/1200px-Zara_Logo.svg.png"
    return render(request, 'blog/zara.html', {'zara_items': zara_items})


def bershka(request):
    bershka_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi')\
        .filter(Q(baslik__contains='Bershka') | Q(baslik__contains='bershka'))
    bershka_image = "http://logo-logos.com/wp-content/uploads/2016/10/Bershka_logo.png"
    return render(request, 'blog/bershka.html', {'bershka_items': bershka_items})
