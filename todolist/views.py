from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, Category

# Create your views here.
def redirect_view(request):
    return redirect("/category")
def todo(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "Add" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/todo")
        if "Delete" in request.POST:
            checkedlist = request.POST.getlist('checkedbox')
            for i in range(len(checkedlist)):
                todo = TodoList.objects.filter(id=int(checkedlist[i]))
                todo.delete()
    return render(request, "todo.html", {"todos": todos, "categories": categories})

def category(request):
    categories = Category.objects.all()
    if request.method == "POST":
        if "Add" in request.POST:
            name = request.POST["name"]
            category = Category(name=name)
            category.save()
            return redirect("/category")
        if "Delete" in request.POST:
            check = request.POST.getlist('check')
            for i in range(len(check)):
                try:
                    сateg = Category.objects.filter(id__in=[int(_id) for _id in check]).delete()
                    сateg.delete()
                except BaseException:
                    return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
        return render(request, "category.html", {"categories": categories})
