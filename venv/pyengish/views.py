
from django.http import HttpResponse

def home_view(request):
    name = 'PAUL'
    HTML_STRING = f"""<h1>HELLO {name}</h1>"""

    return HttpResponse(HTML_STRING)