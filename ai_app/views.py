from django.shortcuts import render,HttpResponse
from face.facmain import face
from mouse.Virtual_Mouse import mouse
from keyboard.demo import key


# from keyboard.virtual keyboard import keyboard

# Create your views here.
def index(request):
    # return HttpResponse("hiii i'm index")
    return render(request,"index.html")

def facefun(request):
    face()
    return HttpResponse("Done")

def virtualfun(request):
    mouse()
    return HttpResponse("By Varun Pal")

def virtualkey(request):
    key()
    return HttpResponse("DONE!!!")
