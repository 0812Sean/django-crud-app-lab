
# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    isbn = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=1000)
    rating = models.IntegerField(default=0)


    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.book.title}"

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.id})
