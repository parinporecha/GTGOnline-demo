# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render_to_response, render
import json
import sys
import datetime

from models import Task


def demo(request):
    print >>sys.stderr, "Entered demo function"
    tasks = []
    for i in Task.objects.all():
        tasks.append({"id":i.id, "name":i.name, "description":i.description, "start_date":i.start_date.strftime('%d/%m/%Y') if i.start_date != None else "", "due_date":i.due_date.strftime('%d/%m/%Y') if i.due_date != None else ""})
    tasks_json = json.dumps(tasks)
    #return render_to_response('demo/demo.html', {'response':response_json})
    template = loader.get_template('demo/demo.html')
    context = RequestContext(request, {'task':tasks_json})
    return HttpResponse(template.render(context))

def create(request):
    print >>sys.stderr, "Entered create function"
    if request.method == 'POST':
        print >>sys.stderr, "request has been identified as POST"
        title = request.POST['title']
        task_description = request.POST['description']
        start = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y').date() if request.POST['start_date'] != '' else None
        due = datetime.datetime.strptime(request.POST['due_date'], '%m/%d/%Y').date() if request.POST['due_date'] != '' else None
        #form = ContactForm(request.POST)
        #if form.is_valid():
            #print >>sys.stderr, "form is valid"
        a = Task(name = title, description = task_description, start_date = start, due_date = due)
        a.save()
        return HttpResponseRedirect('/demo/')
        #else:
            #print >>sys.stderr, "form is invalid"
            #form = ContactForm()
