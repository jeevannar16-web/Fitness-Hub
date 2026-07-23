from django.shortcuts import render, get_object_or_404
from .models import InspirationPost


def inspiration_list(request):
    posts = InspirationPost.objects.all()
    category = request.GET.get('category')

    if category:
        posts = posts.filter(category=category)

    categories = InspirationPost.CATEGORY_CHOICES

    context = {
        'posts': posts,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'inspiration/inspiration_list.html', context)


def inspiration_detail(request, pk):
    post = get_object_or_404(InspirationPost, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'inspiration/inspiration_detail.html', context)
