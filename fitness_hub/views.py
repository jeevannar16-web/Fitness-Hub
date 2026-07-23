from django.shortcuts import render
from exercises.models import Exercise
from inspiration.models import InspirationPost


def home(request):
    context = {
        'featured_exercises': Exercise.objects.all()[:3],
        'recent_inspiration': InspirationPost.objects.all()[:3],
    }
    return render(request, 'home.html', context)
