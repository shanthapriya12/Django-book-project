from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.views.generic import DetailView, ListView

from django.db.models import Q

from .models import Book
from .forms import BookForm


def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('books:book_list')

    else:

        form = AuthenticationForm()

    return render(
        request,
        'books/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    return redirect('books:book_list')


@permission_required(
    'books.view_book',
    raise_exception=True
)
def book_list(request):

    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'books/book_list.html',
        {
            'page_obj': page_obj,
            'query': query
        }
    )
@permission_required(
    'books.add_book',
    raise_exception=True
)
def add_book(request):

    if request.method == 'POST':

        form = BookForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('books:book_list')

    else:
        form = BookForm()

    return render(
        request,
        'books/add_book.html',
        {'form': form}
    )

@permission_required(
    'books.view_book',
    raise_exception=True
)
def book_detail(request, book_id):

    book = get_object_or_404(
        Book,
        id=book_id
    )

    return render(
        request,
        'books/book_detail.html',
        {'book': book}
    )


@login_required
def update_book(request, book_id):

    book = get_object_or_404(
        Book,
        id=book_id
    )

    if request.method == 'POST':

        form = BookForm(
            request.POST,
            request.FILES,
            instance=book
        )

        if form.is_valid():

            form.save()

            return redirect(
                'books:book_detail',
                book_id=book.id
            )

    else:

        form = BookForm(instance=book)

    return render(
        request,
        'books/update_book.html',
        {
            'form': form,
            'book': book
        }
    )


@permission_required(
    'books.delete_book',
    raise_exception=True
)
def delete_book(request, book_id):

    book = get_object_or_404(
        Book,
        id=book_id
    )

    book.delete()

    return redirect('books:book_list')

class BookListView(ListView):

    model = Book

    template_name = 'books/book_list.html'

    context_object_name = 'books'


class BookDetailView(DetailView):

    model = Book

    template_name = 'books/book_detail.html'

    context_object_name = 'book'