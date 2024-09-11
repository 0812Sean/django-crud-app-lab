from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


from .models import Book, Review

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.reviews.all()
    return render(request, 'books/detail.html', {'book': book})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn']
    success_url = '/books/'
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['author', 'summary', 'isbn']

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books/'

class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        return context


class ReviewCreate(CreateView):
    model = Review
    fields = ['reviewer_name', 'review_text', 'rating']

    def form_valid(self, form):
        form.instance.book_id = self.kwargs['book_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.kwargs['book_id']})

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['reviewer_name', 'review_text', 'rating']

class ReviewDelete(DeleteView):
    model = Review

    def get_success_url(self):
        return reverse('book-detail', kwargs={'book_id': self.object.book.id})
