from django.shortcuts import render

from .models import Article
# Create your views here.
def home_view(request):
    return render(request,"home.html",{})

def content(request):
    art1 = Article.objects.get(id=1)
    art2 = Article.objects.get(id=2)
    art3 = Article.objects.get(id=3)
    the_content = {
        'art1':art1,
        'art2':art2,
        'art3':art3,
    }
    return render(request,"article.html",the_content)
