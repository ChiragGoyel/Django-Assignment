from django.contrib.auth.models import User,AbstractUser
from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class CustomUser(AbstractUser):
    Choices = [('librarian','Librarian'),('student','Student')]
    designation = models.CharField(max_length=100, blank=False, choices=Choices)

class Book(models.Model):
    
    id	= models.AutoField(primary_key=True)
    book_id	= models.IntegerField()
    best_book_id	= models.IntegerField()
    work_id	= models.IntegerField()
    books_count	= models.IntegerField()
    isbn	= models.IntegerField()
    isbn13= models.IntegerField()
    authors	= models.CharField(max_length=50)
    original_publication_year	= models.IntegerField()
    original_title	= models.CharField(max_length=100)
    title	= models.CharField(max_length=100)
    language_code	= models.CharField(max_length=20)
    average_rating	= models.FloatField(max_length=3)
    ratings_count = models.IntegerField()
    work_ratings_count	= models.IntegerField()
    work_text_reviews_count	= models.IntegerField()
    ratings_1	= models.IntegerField()
    ratings_2	= models.IntegerField()
    ratings_3	= models.IntegerField()
    ratings_4	= models.IntegerField()
    ratings_5	= models.IntegerField()
    image_url	= models.ImageField(upload_to='images/', blank=True)
    small_image_url = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    
