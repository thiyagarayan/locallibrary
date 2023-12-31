from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance,Genre
from django.views import generic

class BookDetailView(generic.DetailView):
    model = Book
class AuthorDetail(generic.DetailView):
    model = Author
class AuthorList(generic.ListView):
    model = Author
    template_name='authors.html'


class BookListView(generic.ListView):
    model = Book
    template_name = 'books.html'
    
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


