from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Allbooks/', views.BookListView.as_view(), name='All-books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('Allauthors/',views.AuthorList.as_view(),name='all-authors'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author-detail'),
]


