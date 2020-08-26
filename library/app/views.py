from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from django.views.generic import ListView,DetailView
from django.db.models import Q  # Q for multiple search
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import View






###--##--### Home view Start ###--##--###
class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Book
    context_object_name = 'books'

    def get_queryset(self):   
        books = super().get_queryset()
        print(books)
        return books
###--##--### Home view End ###--##--###



###--##--### Book Create View Start ###--##--###
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'create.html'
    fields = ['book_id',	'best_book_id',	'work_id',	'books_count',	'isbn',	'isbn13',	'authors',	'original_publication_year',	'original_title',	'title',	'language_code',	'average_rating',	'ratings_count',	'work_ratings_count',	'work_text_reviews_count',	'ratings_1',	'ratings_2',	'ratings_3',	'ratings_4',	'ratings_5',	'image_url',	'small_image_url']

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.save()
        messages.success(self.request, 'Your book has been successfully created!')
        return redirect('home')
###--##--### Book Create View End ###--##--###


###--##--### Book Update View Start ###--##--###
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'update.html'
    fields = ['book_id','best_book_id',	'work_id',	'books_count',	'isbn',	'isbn13',	'authors',	'original_publication_year',	'original_title',	'title',	'language_code',	'average_rating',	'ratings_count',	'work_ratings_count',	'work_text_reviews_count',	'ratings_1',	'ratings_2',	'ratings_3',	'ratings_4',	'ratings_5',	'image_url',	'small_image_url']
    # success_url = '/'
    def form_valid(self,form):
        instance = form.save()
        messages.success(self.request, 'Your book has been successfully updated!')
        return redirect('home')
###--##--### Book Update View End ###--##--###


###--##--### Book Delete View Start ###--##--###
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = '/'

    def delete(self,request,*args,**kwargs): 
        messages.success(self.request, 'Your book has been successfully deleted!')
        return super().delete(self,request,*args,**kwargs)
###--##--### Book Delete View End ###--##--###


###--##--### Sign Up Start ###--##--###
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home') 

###--##--### Sign Up End ###--##--###



