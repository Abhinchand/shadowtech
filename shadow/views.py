from django.shortcuts import render
import os
from twilio.rest import Client
import logging
# Create your views here.
from django.core.cache import cache
############# home page ###########
logging.basicConfig(filename='logfile.log', encoding='utf-8', level=logging.DEBUG)
def HomePage(request):
    if request.method == 'POST':
        logging.warning('Job started to send message ')
        cache.clear()
        try:
            logging.warning('Try block')
            name = request.POST['contact-name']
            phone = request.POST['contact-phone']
            email = request.POST['contact-email']
            subject = request.POST['subject']
            msg = request.POST['contact-message']
            # print('submit')
            # print(len(phone))
            # print(phone)

            if len(phone) >11:
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
                # print(body)
                logging.warning(body)
        except Exception as e:
            # print('failed',e)
            logging.warning('ERROR '+ str(e))



    return render(request, 'main/index.html')

###########  about me #############
def about_me(request):
    return render(request, 'main/About_Me.html')

def portfolio(request):
    return render(request,'')

