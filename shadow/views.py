from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

############# home page ###########
def HomePage(request):
    return render(request, 'main/index.html')

###########  about me #############
def about_me(request):
    return render(request, 'main/About_Me.html')
##########  After login  ############
@login_required()
def dashboard(request):
    return render(request,'main/Dash.html')
