from django.http import HttpResponse
import platform

def healthz(request):
    return HttpResponse('HTTP 200 OK')

def containerid(request):
    return HttpResponse(platform.node())
