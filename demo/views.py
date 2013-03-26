# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader, RequestContext


def demo(request):
    template = loader.get_template('demo/demo.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

