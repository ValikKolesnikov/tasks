from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Category, TODO
from .forms import ToDoForm
from django.views.decorators.csrf import csrf_exempt


def main_page_view(request):
    if request.method == "POST":
        add_form = ToDoForm(request.POST)
        if add_form.is_valid():
            todo = TODO(text=add_form.data['text'])
            todo.save()
    args = {
        'todos': TODO.objects.all(),
        'add_form': ToDoForm(),
        'category': ''
    }
    return render(request, 'to_do_list/main-page.html', args)


@csrf_exempt
def add_todo_view(request, category_name):
    if request.method == 'POST':
        add_form = ToDoForm(request.POST)
        if add_form.is_valid():
            if category_name == 'default':
                todo = TODO(text=add_form.data['text'])
            else:
                category = get_object_or_404(Category, name=category_name)
                todo = TODO(text=add_form.data['text'], category=category)
            todo.save()
    args = {
        'todos': TODO.objects.all(),
        'add_form': ToDoForm()
    }
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
def edit_todo_view(request, id):
    args = {'id': id}
    task = TODO.objects.get(id=id)
    args['add_form'] = ToDoForm({'text': task.text})
    if request.method == 'POST':
        edit_form = ToDoForm(request.POST)
        if edit_form.is_valid():
            task.text = edit_form.data['text']
            task.save()
            args['add_form'] = ToDoForm({'text': task.text})
    return render(request, 'to_do_list/edit_page.html', args)


@csrf_exempt
def delete_todo_view(request, id):
    task = get_object_or_404(TODO, id=id)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def category_page_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    args = {
        'todos': TODO.objects.filter(category__name=category),
        'add_form': ToDoForm(),
        'category': category
    }
    return render(request, 'to_do_list/main-page.html', args)
