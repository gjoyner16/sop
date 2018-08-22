from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document, Step
from django.utils import timezone

# Create your views here.
def home(request):
    documents = Document.objects
    steps = Step.objects
    return render(request, 'docs/home.html', {'documents':documents})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['application'] and request.POST['title'] and request.POST['type'] and request.POST['description']:
            document = Document()
            document.application = request.POST['application']
            document.client = request.POST['client']
            document.title = (request.POST['title']).capitalize()
            document.type = request.POST['type']
            document.category = request.POST['category']
            document.description = (request.POST['description']).capitalize()
            document.pub_date = timezone.datetime.now()
            document.save()
            return redirect('/docs/detail/'+str(document.id))
        else:
            return render(request, 'docs/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'docs/create.html')

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    steps = Step.objects
    return render(request, 'docs/detail.html',{'document':document, 'steps':steps})

@login_required(login_url="/accounts/signup")
def add_step(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    if request.method == 'POST':
            step = Step()
            step.title = document.title
            step.step_num = request.POST['step_num']
            step.step_nav = request.POST['step_nav']
            step.step_text = request.POST['step_text']
            step.step_note = request.POST['step_note']
            step.step_image = request.FILES['step_image']
            step.save()
            return redirect('/docs/detail/'+str(document.id))
