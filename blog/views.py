from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm, CommentForm, CategoryForm
from .models import Gonderi, Comment, Categories


def post_list(request):
    gonderiler = Gonderi.objects.all().order_by('-olusturma_tarihi')
    query = request.GET.get("q")
    if query:
        gonderiler = gonderiler.filter(baslik__icontains=query)
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
def add_comment_to_post(request, pk):
    post = get_object_or_404(Gonderi, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


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
    posts = Gonderi.objects.filter(olusturma_tarihi__isnull=True). \
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
    zara_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi') \
        .filter(Q(baslik__contains='Zara') | Q(baslik__contains='zara'))
    return render(request, 'blog/zara.html', {'zara_items': zara_items})


def bershka(request):
    bershka_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi') \
        .filter(Q(baslik__contains='Bershka') | Q(baslik__contains='bershka'))
    return render(request, 'blog/bershka.html', {'bershka_items': bershka_items})


def hm(request):
    hm_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi') \
        .filter(Q(baslik__contains='H&M') | Q(baslik__contains='h&m'))
    return render(request, 'blog/hm.html', {'hm_items': hm_items})


def pullnbear(request):
    pullnbear_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi') \
        .filter(Q(baslik__contains='Pull&Bear') | Q(baslik__contains='pull&bear'))
    pullnbear_image = "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg.png"
    return render(request, 'blog/pullnbear.html',
                  {'pullnbear_items': pullnbear_items, 'pullnbear_image': pullnbear_image})


def stradivarius(request):
    stradivarius_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi') \
        .filter(Q(baslik__contains='Stradivarius') | Q(baslik__contains='stradivarius'))
    stradivarius_image = "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg.png"
    return render(request, 'blog/stradivarius.html', {'stradivarius_items': stradivarius_items})


def mango(request):
    mango_items = Gonderi.objects.filter(olusturma_tarihi__lte=timezone.now()).order_by('-olusturma_tarihi') \
        .filter(Q(baslik__contains='Mango') | Q(baslik__contains='mango'))
    mango_image = "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg.png"
    return render(request, 'blog/mango.html', {'mango_items': mango_items})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def list_of_post_by_category(request, category_slug):
    categories = Categories.objects.all()
    post = Gonderi.objects.all()
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        post = post.filter(category=category)
    template = 'blog/category/list_of_post_by_category.html'
    context = {'category': categories, 'post': post, 'category': category}
    return render(request, template, context)