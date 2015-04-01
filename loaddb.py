from shortnames.models import Obj
from shortnames.models import Attribute
from shortnames.models import ObjAtt


objs = {
    'BidRequest': 'bidrequest',
    'Imp': 'imp',
    'Banner': 'banner',
    'Video': 'video',
    'Native': 'native',
    'Site': 'site',
    'App': 'app',
    'Publisher': 'publisher',
    'Content': 'content',
    'Producer': 'producer',
    'Device': 'device',
    'Geo': 'geo',
    'User': 'user',
    'Data': 'data',
    'Segment': 'segment',
    'Regs': 'regs',
    'Pmp': 'pmp',
    'Deal': 'deal'
}


attribs = {
    'bidrequest': 'bq',
    'id': 'id',
    'imp': 'im',
    'site': 'si',
    'app': 'ap',
    'device': 'de',
    'user': 'us',
    'test': 'te',
    'at': 'at',
    'tmax': 'tx',
    'wseat': 'ws',
    'allimps': 'al',
    'cur': 'cu',
    'bcat': 'bc',
    'badv': 'ba',
    'regs': 're',
    'ext': 'ex',
    'banner': 'bn',
    'video': 'vi',
    'native': 'na',
    'displaymanager': 'dm',
    'displaymanagerver': 'dv',
    'instl': 'in',
    'tagid': 'ti',
    'bidfloor': 'bf',
    'bidfloorcur': 'bi',
    'secure': 'se',
    'iframebuster': 'if',
    'pmp': 'pm',
    'w': 'w0',
    'h': 'h0',
    'wmax': 'wx',
    'hmax': 'hx',
    'wmin': 'wn',
    'hmin': 'hn',
    'btype': 'bt',
    'battr': 'br',
    'pos': 'po',
    'mimes': 'mi',
    'topframe': 'tf',
    'expdir': 'ed',
    'api': 'ai',
    'minduration': 'nd',
    'maxduration': 'xd',
    'protocol': 'pl',
    'protocols': 'ps',
    'startdelay': 'sd',
    'linearity': 'li',
    'sequence': 'sq',
    'maxextended': 'xe',
    'minbitrate': 'nb',
    'maxbitrate': 'xb',
    'boxingallowed': 'bl',
    'playbackmethod': 'pb',
    'delivery': 'dl',
    'companionad': 'ca',
    'companiontype': 'ct',
    'request': 'rq',
    'ver': 'vr',
    'name': 'nm',
    'domain': 'do',
    'cat': 'cc',
    'sectioncat': 'sc',
    'pagecat': 'pc',
    'page': 'pg',
    'ref': 'rf',
    'search': 'sr',
    'mobile': 'mo',
    'privacypolicy': 'pp',
    'publisher': 'pu',
    'content': 'co',
    'keywords': 'kw',
    'episode': 'ep',
    'title': 'tt',
    'series': 'ss',
    'season': 'sn',
    'producer': 'pd',
    'url': 'ul',
    'videoquality': 'vq',
    'context': 'cx',
    'contentrating': 'cg',
    'userrating': 'ur',
    'qagmediarating': 'qm',
    'livestream': 'ls',
    'sourcerelationship': 'sp',
    'len': 'ln',
    'language': 'la',
    'embeddable': 'em',
    'ua': 'ua',
    'geo': 'ge',
    'dnt': 'dn',
    'lmt': 'lm',
    'ip': 'ip',
    'ipv6': 'i6',
    'devicetype': 'dt',
    'make': 'mk',
    'model': 'md',
    'os': 'os',
    'osv': 'ov',
    'hwv': 'hw',
    'ppi': 'pi',
    'pxratio': 'px',
    'js': 'js',
    'flashver': 'fv',
    'carrier': 'ci',
    'connectiontype': 'cn',
    'ifa': 'ia',
    'didsha1': 'd1',
    'didmd5': 'd5',
    'dpidsha1': 'p1',
    'dpidmd5': 'p5',
    'macsha1': 'm1',
    'macmd5': 'm5',
    'lat': 'lt',
    'lon': 'lo',
    'type': 'ty',
    'country': 'cr',
    'region': 'rg',
    'regionfips104': 'r1',
    'metro': 'me',
    'city': 'cy',
    'zip': 'zi',
    'utcoffset': 'ut',
    'buyerid': 'by',
    'yob': 'yo',
    'gender': 'gn',
    'customdata': 'cd',
    'data': 'da',
    'segment': 'sg',
    'value': 'va',
    'coppa': 'cp',
    'private_auction': 'pa',
    'deals': 'ds',
    'wadomain': 'wa',
    'bundle': 'bu',
    'storeurl': 'st',
    'paid': 'py'
}

bidrequest = [
    'id',
    'imp',
    'site',
    'app',
    'device',
    'user',
    'test',
    'at',
    'tmax',
    'wseat',
    'allimps',
    'cur',
    'bcat',
    'badv',
    'regs',
    'ext'
]

imp = [
    'id',
    'banner',
    'video',
    'native',
    'displaymanager',
    'displaymanagerver',
    'instl',
    'tagid',
    'bidfloor',
    'bidfloorcur',
    'secure',
    'iframebuster',
    'pmp',
    'ext'
]

banner = [
    'w',
    'h',
    'wmax',
    'hmax',
    'wmin',
    'hmin',
    'id',
    'btype',
    'battr',
    'pos',
    'mimes',
    'topframe',
    'expdir',
    'api',
    'ext'
]

video = [
    'mimes',
    'minduration',
    'maxduration',
    'protocol',
    'protocols',
    'w',
    'h',
    'startdelay',
    'linearity',
    'sequence',
    'battr',
    'maxextended',
    'minbitrate',
    'maxbitrate',
    'boxingallowed',
    'playbackmethod',
    'delivery',
    'pos',
    'companionad',
    'api',
    'companiontype',
    'ext'
]

native = [
    'request',
    'ver',
    'api',
    'battr',
    'ext'
]

site = [
    'id',
    'name',
    'domain',
    'cat',
    'sectioncat',
    'pagecat',
    'page',
    'ref',
    'search',
    'mobile',
    'privacypolicy',
    'publisher',
    'content',
    'keywords',
    'ext'
]

app = [
    'id',
    'name',
    'bundle',
    'domain',
    'storeurl',
    'cat',
    'sectioncat',
    'pagecat',
    'ver',
    'privacypolicy',
    'paid',
    'publisher',
    'content',
    'keywords',
    'ext'
]

publisher = [
    'id',
    'name',
    'cat',
    'domain',
    'ext'
]

content = [
    'id',
    'episode',
    'title',
    'series',
    'season',
    'producer',
    'url',
    'cat',
    'videoquality',
    'context',
    'contentrating',
    'userrating',
    'qagmediarating',
    'keywords',
    'livestream',
    'sourcerelationship',
    'len',
    'language',
    'embeddable',
    'ext'
]

producer = [
    'id',
    'name',
    'cat',
    'domain',
    'ext'
]

device = [
    'ua',
    'geo',
    'dnt',
    'lmt',
    'ip',
    'ipv6',
    'devicetype',
    'make',
    'model',
    'os',
    'osv',
    'hwv',
    'h',
    'w',
    'ppi',
    'pxratio',
    'js',
    'flashver',
    'language',
    'carrier',
    'connectiontype',
    'ifa',
    'didsha1',
    'didmd5',
    'dpidsha1',
    'dpidmd5',
    'macsha1',
    'macmd5',
    'ext'
]

geo = [
    'lat',
    'lon',
    'type',
    'country',
    'region',
    'regionfips104',
    'metro',
    'city',
    'zip',
    'utcoffset',
    'ext'
]

user = [
    'id',
    'buyerid',
    'yob',
    'gender',
    'keywords',
    'customdata',
    'geo',
    'data',
    'ext'
]

data = [
    'id',
    'name',
    'segment',
    'ext'
]

segment = [
    'id',
    'name',
    'value',
    'ext'
]

regs = [
    'coppa',
    'ext'
]

pmp = [
    'private_auction',
    'deals',
    'ext'
]

deal = [
    'id',
    'bidfloor',
    'bidfloorcur',
    'at',
    'wseat',
    'wadomain',
    'ext'
]

objatts = {
    'bidrequest': bidrequest,
    'imp': imp,
    'banner': banner,
    'video': video,
    'native': native,
    'site': site,
    'app': app,
    'publisher': publisher,
    'content': content,
    'producer': producer,
    'device': device,
    'geo': geo,
    'user': user,
    'data': data,
    'segment': segment,
    'regs': regs,
    'pmp': pmp,
    'deal': deal
}


def load_objs():
    for k, v in objs.iteritems():
        Obj.objects.create(name=k, short=v)


def load_attribs():
    for k, v in attribs.iteritems():
        Attribute.objects.create(attribute=k, short=v)


def load_objatts():
    for k, v in objatts.iteritems():
        try:
            o = Obj.objects.filter(short=k)[0]
        except Exception:
            print 'Object not found: %s' % k
            continue

        for value in v:
            try:
                a = Attribute.objects.filter(attribute=value)[0]
            except Exception:
                print 'Attribute not found: %s' % value
                continue

            ObjAtt.objects.create(obj=o, att=a)


def load_all():
    Attribute.objects.all().delete()
    Obj.objects.all().delete()
    load_objs()
    load_attribs()
    load_objatts()
