# from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('books/<int:book_id>/reviews/add/', views.ReviewCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/edit/', views.ReviewUpdate.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review-delete'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),

]
