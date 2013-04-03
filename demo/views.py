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
        tasks.append({"id":i.id, "name":i.name, "description":i.description, "start_date":i.start_date.strftime('%d/%m/%Y') if i.start_date != None else "", "due_date":i.due_date.strftime('%d/%m/%Y') if i.due_date != None else "",
                      "done":i.done, "dismissed":i.dismissed})
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
            
def mark_done(request, task_id):
    print >>sys.stderr, "Task id is " + str(task_id)
    print >>sys.stderr, int(task_id)
    a = Task.objects.get(id = task_id)
    a.done = 1
    a.dismissed = 0
    a.save()
    return HttpResponseRedirect('/demo/')
    
def mark_dismissed(request, task_id):
    print >>sys.stderr, "Task id is " + str(task_id)
    print >>sys.stderr, int(task_id)
    a = Task.objects.get(id = task_id)
    a.dismissed = 1
    a.done = 0
    a.save()
    return HttpResponseRedirect('/demo/')

def mark_active(request, task_id):
    print >>sys.stderr, "Task id is " + str(task_id)
    print >>sys.stderr, int(task_id)
    a = Task.objects.get(id = task_id)
    a.done = 0
    a.dismissed = 0
    a.save()
    return HttpResponseRedirect('/demo/')

def delete(request, task_id):
    print >>sys.stderr, "Task id is " + str(task_id)
    print >>sys.stderr, int(task_id)
    a = Task.objects.get(id = task_id)
    a.delete()
    return HttpResponseRedirect('/demo/')

