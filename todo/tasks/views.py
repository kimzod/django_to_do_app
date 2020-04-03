from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('-created')

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'tasks/index.html', context)


def update(request, pk):

    task = Todo.objects.get(id=pk)

    # 작성한Todo 글을 가져온다.
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form': form}

    return render(request, 'tasks/update.html', context)


def delete(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect("/")

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
