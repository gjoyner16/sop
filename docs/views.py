from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document, Step, ClientFolder, CategoryFolder
from django.utils import timezone

# Create your views here.
@login_required(login_url="/accounts/signup")
def home(request):
    clientfolders = ClientFolder.objects
    categoryfolders = CategoryFolder.objects
    documents = Document.objects.all().order_by('pub_date')
    return render(request, 'docs/home.html', {'documents':documents, 'clientfolders':clientfolders, 'categoryfolders':categoryfolders})

@login_required(login_url="/accounts/signup")
def client(request, clientfolder_id):
    clientfolder = get_object_or_404(ClientFolder, pk=clientfolder_id)
    clientfolders = ClientFolder.objects
    categoryfolders = CategoryFolder.objects
    documents = Document.objects.all().order_by('pub_date')
    return render(request, 'docs/client.html', {'clientfolder':clientfolder, 'clientfolders':clientfolders, 'categoryfolders':categoryfolders, 'documents':documents, 'clientfolder_id':clientfolder_id})

@login_required(login_url="/accounts/signup")
def category(request, categoryfolder_id):
    categoryfolder = get_object_or_404(CategoryFolder, pk=categoryfolder_id)
    clientfolders = ClientFolder.objects
    categoryfolders = CategoryFolder.objects
    documents = Document.objects.all().order_by('pub_date')
    return render(request, 'docs/category.html', {'categoryfolder':categoryfolder, 'clientfolders':clientfolders, 'categoryfolders':categoryfolders, 'documents':documents, 'categoryfolder_id':categoryfolder_id})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['application'] and request.POST['title'] and request.POST['type'] and request.POST['description']:
            document = Document()
            document.application = request.POST['application']
            document.title = (request.POST['title']).capitalize()
            document.type = request.POST['type']
            document.description = (request.POST['description']).capitalize()
            document.pub_date = timezone.datetime.now()
            document.creator = request.user
            document.save()
            return redirect('/docs/detail/'+str(document.id))
        else:
            return render(request, 'docs/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'docs/create.html')

@login_required(login_url="/accounts/signup")
def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    steps = Step.objects.all().order_by('step_num')
    return render(request, 'docs/detail.html', {'document':document, 'steps':steps})

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
