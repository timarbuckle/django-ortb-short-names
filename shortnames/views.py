from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
import json

from lib.jsonpath import JsonPath
from .models import Attribute


def index(request):
    return HttpResponse('nothing here, move along')


def show_json_keynames(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            received_json_data = json.loads(request.FILES['file'].read())
            jp = JsonPath()
            jpdata = jp.convert(received_json_data)
            data = _convert_to_short(jpdata)
            context = {'data': data}
            return render(request, 'keynames.html', context)
        else:
            return HttpResponse('Invalid form')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def _convert_to_short(data):
    out = []
    for row in data:
        longkey = row[0]
        keys = longkey.split('.')
        short = ''
        for key in keys:
            short = short + _get_short(key)
        out.append({'long': longkey, 'data': row[1], 'short': short})
    return out


def _get_short(key):
    try:
        att = Attribute.objects.filter(attribute=key)[0]
        out = att.short
    except Exception:
        out = 'unknown'
    return out
