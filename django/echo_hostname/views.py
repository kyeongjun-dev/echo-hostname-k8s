from django.http import HttpResponse
import os
def index(request):
    print(request.META.get('version'))
    hostname = os.getenv('HOSTNAME')
    version = request.headers.get('Version')
    django_version = os.getenv('VERSION')
    region = os.popen('curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone').read()
    return HttpResponse(f'django: {hostname}<br/>version: {django_version}<br/>header version: {version}<br/>Pod region: {region}')

def api(request):
    hostname = os.getenv('HOSTNAME')
    version = request.headers.get('Version')
    django_version = os.getenv('VERSION')
    request_url = os.getenv('REQUEST_URL')
    region = os.popen('curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone').read()
    curl_response = os.popen(f'curl {request_url}').read()
    return HttpResponse(f'django: {hostname}<br/>version: {django_version}<br/>header version: {version}<br/>Pod region: {region}<br/><br/>api_response: <br/>{curl_response}')