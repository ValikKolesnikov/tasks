from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, ToDo
from .forms import ToDoForm
from django.views.decorators.csrf import csrf_exempt


def add_tags_to_todo(tags, todo):
    if todo.tags.all():
        for tag in tags:
            if tag not in todo.tags.all():
                todo.tags.add(tag)
        for tag in todo.tags.all():
            if tag not in tags:
                todo.tags.remove(tag)
    else:
        for tag in tags:
            todo.tags.add(tag)


def main_page_view(request):
    args = {
        'todos': ToDo.objects.all(),
        'add_form': ToDoForm()
    }
    return render(request, 'todos/main-page.html', args)


def add_todo_view(request):
    args = {'add_form': ToDoForm(),
            'todos': ToDo.objects.all()}
    if request.method == 'POST':
        add_form = ToDoForm(request.POST)
        if add_form.is_valid():
            text, category, tags = add_form.cleaned_data.values()
            todo = ToDo(text=add_form.cleaned_data['text'])
            if category:
                todo.category = category
            todo.save()
            if tags:
                add_tags_to_todo(tags=tags, todo=todo)
        else:
            args['add_form'] = add_form
            return render(request, 'todos/main-page.html', args)
        return redirect('main_page_view')


def edit_todo_view(request, id):
    args = {'id': id}
    todo = ToDo.objects.get(id=id)
    if request.method == 'POST':
        edit_form = ToDoForm(request.POST)
        if edit_form.is_valid():
            text, category, tags = edit_form.cleaned_data.values()
            todo.text = text
            todo.category = category
            todo.save()
            add_tags_to_todo(tags=tags, todo=todo)
            return redirect('main_page_view')
        else:
            args['edit_form'] = edit_form
            return render(request, 'todos/edit_page.html', args)
    else:
        args['edit_form'] = ToDoForm({'text': todo.text,
                                      'tags': todo.tags.all(),
                                      'category': todo.category})
        return render(request, 'todos/edit_page.html', args)


def delete_todo_view(request, id):
    task = get_object_or_404(ToDo, id=id)
    task.delete()
    return redirect('main_page_view')


def category_page_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    args = {
        'todos': ToDo.objects.filter(category=category),
        'add_form': ToDoForm()
    }
    return render(request, 'todos/main-page.html', args)
