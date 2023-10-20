from django.http import HttpResponse
from django.shortcuts import render
from .models import Subject,Note

# Create your views here.


def home(request):
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    subjects = Subject.objects.filter(name__icontains = search)
    context = {'subjects':subjects}
    return render(request,'notes/home.html',context)

def notes(request,sid):
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    print(search)
    subject = Subject.objects.get(id = sid)
    notes = subject.note_set.filter(heading__icontains = search)
    context = {'notes':notes,'subject':subject}
    return render(request,'notes/note.html',context)
