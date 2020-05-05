from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
import imaplib
import email
import html5lib
from email.header import Header, decode_header, make_header
from rest_framework.decorators import api_view
from .models import *
from .serializers import SettingsSerialaizer




try:
    password_email = SettingsForRequest.objects.last().password
    email_send = SettingsForRequest.objects.last().email
except: pass
SERVER = "imap.mail.ru"
SMTP_PORT = 993

@api_view(['GET', 'POST', 'PUT'])
def get_save_settings(request):
  

    if request.method == 'POST':
        try:
            serializer = SettingsSerialaizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            print(e, '!!!!!!!Errors')
        return Response(status.HTTP_201_CREATED)
    elif request.method == "GET":
        my_settings = SettingsForRequest.objects.last()
        data = {'email': email_send, 'password': password_email, 'timeForSend': '1',
                'rangTodo': '2'}
        return Response(data)
    else:
        my_settings = SettingsForRequest.objects.last()
        serializer = SettingsSerialaizer(my_settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def shownewsmail(request):
    themenews = request.GET.get('q', '').split(',')
    doc = {}
    count = 1
    for interes in themenews:
        query = f'https://habr.com/ru/search/?target_type=posts&q={interes}&order_by=date'
        r = requests.get(query)
        soup = BeautifulSoup(r.text, 'html5lib')  # instead of html.parser
        if not soup.find("h2", {"class": "post__title"}):
            doc['status'] = 'title_not_found'
        else:
            for el in soup.find_all("a", {"class": "post__title_link"})[:7]:
                doc[str(count)] = str(el)
                count += 1

    return Response(doc)




@api_view(['GET'])
def get_email(request):
    
    try:
        mail = imaplib.IMAP4_SSL(SERVER)
        mail.login(email_send, password_email)
        mail.select('Inbox')
        status, select_data = mail.select('INBOX')
        type, data = mail.search(None, 'ALL') 

        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1]) 
        key = 1
        myemail = {}
        for i in range(latest_email_id, first_email_id, -1)[:10]:
            try:
                typ, data = mail.fetch(str(i), '(RFC822)')
            except Exception as e:
                print(e)

            for response_part in data:
                if isinstance(response_part, tuple):
                    try:
                        msg = email.message_from_string(
                            response_part[1].decode('utf-8'))
                    except Exception as e: 
                        print(e)
                    email_subject = msg['subject']
                    email_from = msg['from']
                    # print('From : ' + str(make_header(decode_header(email_from))) + '\n')
                    # print('Subject : ' + str(make_header(decode_header(email_subject))) + '\n')
                    myemail[key] = [str(make_header(decode_header(email_from))),
                                    'Тема : ' + str(make_header(decode_header(email_subject)))]


                    key += 1
    except:
        pass

    try:
        return Response(myemail)
    except: return Response('Error') 
    
