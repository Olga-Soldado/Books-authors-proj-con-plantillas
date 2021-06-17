from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def createBooks(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def createAuthors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def processBook(request):
    Book.objects.create(
        title = request.POST['book-title'],
        desc = request.POST['book-description']
    )
    return redirect('/')

def processAuthor(request):
    Author.objects.create(
        first_name = request.POST['author-first-name'],
        last_name = request.POST['author-last-name'],
        notas = request.POST['author-notes']
    )
    return redirect('/authors')

def displayBook(request, book_id):
    the_books = Book.objects.get(id=book_id)
    all_authors = Author.objects.exclude(books__id=book_id)
    context = {
        'book': the_books,
        'all_authors': all_authors,
    }
    return render(request, 'displayBooks.html', context)

def displayAuthor(request, author_id):
    the_authors = Author.objects.get(id=author_id)
    all_books = Book.objects.exclude(author__id=author_id)
    context ={
        'author': the_authors,
        'all_books': all_books,
    }
    return render(request, 'displayAuthors.html', context)

def addAuthor(request, book_id):
    this_author = Author.objects.get(id=request.POST['author-to-add'])
    Book.objects.get(id=book_id).author.add(this_author)
    return redirect(f'/books/{book_id}')

def addBook(request, author_id):
    this_book = Book.objects.get(id=request.POST['book-to-add'])
    Author.objects.get(id=author_id).books.add(this_book)
    return redirect(f'/authors/{author_id}')
