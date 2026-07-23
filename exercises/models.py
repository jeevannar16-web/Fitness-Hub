from django.db import models


class Exercise(models.Model):
    MUSCLE_CHOICES = [
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('shoulders', 'Shoulders'),
        ('biceps', 'Biceps'),
        ('triceps', 'Triceps'),
        ('legs', 'Legs'),
        ('glutes', 'Glutes'),
        ('core', 'Core'),
        ('cardio', 'Cardio'),
        ('full_body', 'Full Body'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50, choices=MUSCLE_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    instructions = models.TextField(blank=True)
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text='YouTube or other video URL')
    sets = models.PositiveIntegerField(default=3)
    reps = models.CharField(max_length=20, default='10-12')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
