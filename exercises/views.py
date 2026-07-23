from django.shortcuts import render, get_object_or_404
from .models import Exercise


def exercise_list(request):
    exercises = Exercise.objects.all()
    muscle_group = request.GET.get('muscle_group')
    difficulty = request.GET.get('difficulty')

    if muscle_group:
        exercises = exercises.filter(muscle_group=muscle_group)
    if difficulty:
        exercises = exercises.filter(difficulty=difficulty)

    context = {
        'exercises': exercises,
        'muscle_choices': Exercise.MUSCLE_CHOICES,
        'difficulty_choices': Exercise.DIFFICULTY_CHOICES,
        'selected_muscle': muscle_group,
        'selected_difficulty': difficulty,
    }
    return render(request, 'exercises/exercise_list.html', context)


def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    related = Exercise.objects.filter(muscle_group=exercise.muscle_group).exclude(pk=pk)[:3]
    context = {
        'exercise': exercise,
        'related': related,
    }
    return render(request, 'exercises/exercise_detail.html', context)
