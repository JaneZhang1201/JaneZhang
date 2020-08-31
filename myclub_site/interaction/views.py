from django.shortcuts import render

from interaction.forms import FeedbackForm

def contect(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }
    return render(request,"contect.html",context)
# Create your views here.
