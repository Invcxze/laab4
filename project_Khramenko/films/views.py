from django.shortcuts import render,redirect,HttpResponse
from .models import Films
from .forms import FilmsForms
def index(request):
    films = Films.objects.all()
    return render(request,'films\index.html',{'films':films})

def add(request):
    if request.method == "POST":
        form = FilmsForms(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            actors = request.POST.get('actors')            
            category_id =request.POST.get('category_id')
            Date_showed =request.POST.get('Date_showed')
            Films.objects.create(title=title,actors=actors,category_id=category_id,Date_showed=Date_showed)
            return redirect('../')   
    form =  FilmsForms()
    return render(request,'Films\\add.html',{'form':form})


def delete(request,num):
    delete_articles = Films.objects.get(id = num)
    if not delete_articles:
        return HttpResponse('такой записи в бд нет')
    else:
        delete_articles.delete()
    return redirect('../')

def edit(request,num):
    try:
        articles = Films.objects.get(id=num)
 
        if request.method == "POST":
            form = FilmsForms(request.POST)
            if form.is_valid():
                articles.title = request.POST.get('title')
                articles.actors = request.POST.get('actors')
                articles.category_id = request.POST.get('category_id')
                articles.Date_showed = request.POST.get('date_showed')
                articles.save()
                return redirect("../")
        else:
            form = FilmsForms() 
            return render(request,'Films\edit.html',{'form':form})
    except articles.DoesNotExist:
        return HttpResponse("<h2>Person not found</h2>")
     