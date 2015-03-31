from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import UploadFileForm
import json

from lib.jsonpath import JsonPath
from .models import Attribute


def index(request):
    return HttpResponse('nothing here, move along')


def _link(filename):
    return {'link': filename, 'name': filename.split('.')[0]}


def demos(request):
    data = [
        _link("expandable_creative.json"),
        _link("mobile.json"),
        _link("native_ad.json"),
        _link("pmp_direct_deal.json"),
        _link("simple_banner.json"),
        _link("video.json")
    ]
    context = {'data': data}
    return render(request, 'demos.html', context)


def demo_file(request, filename):
    fullpathname = '%s/tests/%s.json' % (settings.BASE_DIR, filename)
    f = open(fullpathname, 'r')
    json_data = json.loads(f.read())
    f.close()
    jp = JsonPath()
    jpdata = jp.convert(json_data)
    data = _convert_to_short(jpdata)
    context = {'data': data}
    return render(request, 'keynames.html', context)


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
