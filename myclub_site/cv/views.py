from django.shortcuts import render

from cv.models import Cv

def cv(request):
    obj = Cv.objects.get(id=2)
    the_content = {
        'obj':obj.photo,
        }
    return render(request,"cv.html",the_content)
# Create your views here.
