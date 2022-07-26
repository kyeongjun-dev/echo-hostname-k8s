from django.http import HttpResponse
import os
def index(request):
    print(request.META.get('version'))
    version = request.headers.get('Version')
    django_version = os.getenv('VERSION')
    return HttpResponse(f'<br/>django: echo-hostname-backned<br/>version: {django_version}<br/>header version: {version}')
