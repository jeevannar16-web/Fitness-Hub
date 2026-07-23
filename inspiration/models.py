from django.db import models


class InspirationPost(models.Model):
    CATEGORY_CHOICES = [
        ('quote', 'Quote'),
        ('tip', 'Fitness Tip'),
        ('story', 'Success Story'),
        ('motivation', 'Motivation'),
    ]

    title = models.CharField(max_length=200)
    quote = models.TextField()
    author = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='quote')
    image = models.ImageField(upload_to='inspiration/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
