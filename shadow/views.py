from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import os
from twilio.rest import Client
import logging
# Create your views here.
from django.core.cache import cache
from .forms import *
from django.contrib.auth.decorators import login_required
############# home page ###########
from shadowtech import settings
ROOT_URL = settings.ROOT_URL

@login_required()
def admin_page(request):
    data = Message.objects.all()
    context ={
        'message_data':data
    }
    return render(request,'admin/inbox.html',context)

@login_required()
def new_inbox(request):
    data = Message.objects.filter(status=False)
    context ={
        'message_data':data
    }
    return render(request,'admin/new_inbox.html',context)


@login_required()
def read_message(request,id=None):
    instance = get_object_or_404(Message, id=id)
    instance.status=True
    instance.save()

    return redirect('admin_page')
@login_required()
def delete_message(request,id=None):
    instance = get_object_or_404(Message, id=id)
    instance.delete()

    return redirect('admin_page')

def HomePage(request):
    if request.method == 'POST':
        file1 = open('myfile.txt', 'w')
        file1.write('Job started to send message\n')
        cache.clear()
        try:

            file1.write('Job started with try block\n')
            # logging.warning('Try block')
            name = request.POST['name']
            phone = request.POST['phone_no']
            email = request.POST['email']
            subject = request.POST['subject']
            msg = request.POST['content']
            form = Message_form(request.POST)

            if form.is_valid():
                form.save()

                file1.write('Form saved\n')

            if len(phone) >11:
                file1.write('valid phone number\n')
                logging.warning('valid ph number')
                account_sid = 'AC3adeba580965764c56c76a3a08b10dc3'
                auth_token = '8cf11f4279f9b09e293b349ceed17e05'
                client = Client(account_sid, auth_token)

                body = f'Hi {name} \n Your contact request has been received with message -  \n Subject -{subject} \n Message - {msg} \n Thank You'
                message = client.messages.create(
                    body=body,
                    from_='+15188325100',
                    to=phone
                )

                file1.write('Message has been sended\n')
                # print(body)
        except Exception as e:
            pass
            file1.write(f'Error {e}\n')

        # Closing file
        file1.close()
    context = {
        'ROOT_URL': ROOT_URL
    }

    return render(request, 'main/index.html',context)





###########  about me #############
def about_me(request):
    return render(request, 'main/About_Me.html')

def portfolio(request):
    return render(request,'')

def google_site_verf(request):
    return render(request, 'main/google895d8fb8741a4b5c.html')

def robo_file(request):
    return render(request, 'main/robots.txt')