from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.urls import path, include

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books':books})

def show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/show.html', {'books':book})    

def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('books:index')
    
    return render(request, 'books/add.html', {'form':form})

def edit(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('books:index')
    
    return render(request, 'books/edit.html', {'form':form})


def delete(request):
    book = get_object_or_404(Book, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功')
        return redirect('books:index')
    
    return render(request, 'books/delete.html', {'form':form})

