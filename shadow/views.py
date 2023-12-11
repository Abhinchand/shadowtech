from django.shortcuts import render

# Create your views here.

############# home page ###########
def HomePage(request):
    return render(request, 'main/index.html')

###########  about me #############
def about_me(request):
    return render(request, 'main/About_Me.html')

def portfolio(request):
    return render(request,'')