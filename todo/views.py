from django.shortcuts import render
import random

from todo.models import Category, Todo

# Create your views here.


def home(request):
    todo_query_set = Todo.objects.all().filter(completed=False)

    # 2 ta dan kop bolsa
    todo1 = todo_query_set[1]
    todo0 = todo_query_set.first()
    todolast = todo_query_set.last()
    todofield = todo_query_set.values()

    context = {
        "random": random.randint(1, 100),
        "todo_query_set": todo_query_set.values_list(),
        "todo1": todo1,
        "todo0": todo0,
        "todol": todolast,
        "todofield": todofield,
    }

    return render(request, "index.html", context=context)
