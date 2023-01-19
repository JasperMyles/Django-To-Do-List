from django.shortcuts import render, redirect
from .models import Todo
from .forms import createTodo
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'todo/homepage.html')

# Needed to view that page
@login_required(login_url='accounts:login')

def todolist_home(request):
    todos = Todo.objects.all()
    
    context = {'name': 'david',
               'age': 34,
               'is_Married': 'Not yet',
               'todos': todos
               }
    return render(request, 'todo/todolist_home.html', context )

# Needed to view that page
@login_required(login_url='accounts:login')
def todo_create(request):
    form = createTodo()
    context = {
        'form': form
    }
    if request.method ==  'POST':
        form = createTodo(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # print(form.cleaned_data['title'])
            # print(form.cleaned_data['body'])
            print(request.user)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            
    
    return render(request, 'todo/todo_create.html', context)

def todo_update(request, pk):
    print(pk)
    todo = Todo.objects.get(id=pk)
    form = createTodo(request.POST or None, instance =todo)
    if form.is_valid():
         form.save()
    context = {
        # 'todo': todo
        'form':form
    }
    return render(request, 'todo/todo_update.html', context)
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo:todo_list')

