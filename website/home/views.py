from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("home/index.html")
    context = {'dummy_context':"This is a dummy context"}

    return HttpResponse(template.render(context, request))
