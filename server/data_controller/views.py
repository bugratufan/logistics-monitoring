from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
import unicodedata
import re
import os

class Data(object):
    pass



def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def data_saver(request):
    if(request.GET.get('data') is None): # Tracker comm
        return HttpResponse("data error", status = 200)
    elif(request.GET.get('user') is not None):
        username = slugify(request.GET.get('user'))
        try:
            print("./../data/"+username)
            os.makedirs("./../data/"+username)
        except Exception as e:
            print(e)
        f = open("./../data/"+username+"/data","a")
        f.write(str(request.GET.get('data'))+"\n")
        f.close()
        return HttpResponse(request.GET.get('data'), status = 200)
    else:
        return HttpResponse("user error", status = 200)

def map(request):
    data = Data()
    data.temp = 15
    data.speed = 30
    return TemplateResponse(request, 'map.html', {'data': data})


# def data_table(request):
#     if(request.GET.get('user') is None): # Tracker comm
#         return HttpResponse("user error", status = 200)
#     else:
#         username = slugify(request.GET.get('user'))
#         lines = readlines("./../data/"+username+"/data")
#
#
#         f = open("./../data/"+username+"/data","r")
#         f.write(str(request.GET.get('data'))+"\n")
#         f.close()
#         return HttpResponse(request.GET.get('data'), status = 200)
#     else:
#         return HttpResponse("user error", status = 200)
