from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line
import sys



settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],  # Allows all hosts during development
    SECRET_KEY = 'your_secret_key_here',
)

def index(request):
    print('hello')
    print('Got request from', request.GET.get('name', 'Anonymous'))
    height = int(request.GET.get('height', 10))
    x = '& '
    for i in range(height):
        x += '<br>' + i * '&&'
    return HttpResponse(x)

urlpatterns = [
    path('', index),
]

application = get_wsgi_application()

if __name__ == '__main__':
    execute_from_command_line(sys.argv)

