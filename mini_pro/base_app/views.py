from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post


def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).ordered_by('published_date')
    return render(request, 'base_app/post_list.html', {'post': post})
