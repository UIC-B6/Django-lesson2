from django.shortcuts import render
import random

from todo.models import Category, Todo

# Create your views here.


def home(request):
    todo_query_set = Todo.objects.all()

    # 2 ta dan kop bolsa 
    todo1 = todo_query_set[1]


    context = {
        "random":random.randint(1,100),
        "todo_query_set":todo_query_set,
        "todo": todo1
    }

    return render (request, "index.html", context=context)
