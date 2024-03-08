from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("home/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
