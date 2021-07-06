from myapp.models import Image
from myapp.forms import ImageForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = ImageForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/index.html', {'img':img, 'form':fm})

# This will delete the image
def delete(request, id):
    if request.method == 'POST':
        pi = Image.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
