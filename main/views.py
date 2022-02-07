from django.shortcuts import render

# Create your views here.
def homeView(request):
    context = None
    return render(request,'main/home.html',context)