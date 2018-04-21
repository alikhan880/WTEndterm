from django.shortcuts import render, redirect
from django.http import QueryDict, HttpResponseRedirect
from .models import Category, Book
from django.urls import reverse
# Create your views here.

def index(request):
	return render(request, 'index.html')

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'category_list.html', {"categories" : categories})

def category_detail(request, category_id):
	books = Book.objects.filter(category_id = category_id)
	return render(request, 'book_list.html', {"books" : books, "category_id" : category_id})

def new_category(request):
	return render(request, 'new_category.html')

def add_category(request):
	data = request.POST
	c = Category()
	c.title = data.get('title', '')
	c.save()
	return redirect('category_list')

def edit_category(request, category_id):
	c = Category.objects.get(pk = category_id)
	return render(request, 'edit_category.html', {"category" : c})

def save_category(request, category_id):
	c = Category.objects.get(pk = category_id)
	data = request.POST
	c.title = data.get('title', c.title)
	c.save()
	return redirect('category_list')

def delete_category(request, category_id):
	c = Category.objects.get(pk = category_id)
	c.delete()
	return redirect('category_list')

def new_book(request, category_id):
	return render(request, 'new_book.html', {'category_id' : category_id})

def add_book(request, category_id):
	data = request.POST
	b = Book()
	c = Category.objects.get(pk = category_id)
	b.title = data.get('title', '')
	b.author = data.get('author', '')
	b.category_id = c
	b.save()
	return redirect(reverse('category_detail', kwargs={"category_id": category_id}))

def edit_book(request, category_id, book_id):
	b = Book.objects.get(pk = book_id)
	return render(request, 'edit_book.html', {"category_id" : category_id, "book" : b,})

def save_book(request, category_id, book_id):
	b = Book.objects.get(pk = book_id)
	c = Category.objects.get(pk=category_id)
	data = request.POST
	b.title = data.get('title', b.title)
	b.author = data.get('author', b.author)
	b.category_id = c
	b.save()
	return redirect(reverse('category_detail', kwargs={"category_id": category_id}))

def delete_book(request, category_id, book_id):
	b = Book.objects.get(pk = book_id)
	b.delete()
	return redirect(reverse('category_detail', kwargs={"category_id": category_id}))

