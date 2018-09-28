from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import *
from .render import Render

#Clients
class ClientList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    model = Client
    context_object_name = 'clients'

class ClientCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Client
    form_class = ClientForm

    def get_initial(self):
        user = self.request.user
        return {
            'user':user,
        }

class ClientUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Client
    fields = ['name', 'icon']
    template_name_suffix = '_update_form'

class ClientDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Client
    success_url = reverse_lazy('client_list')


#Categories
class ClientDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    template_name = 'docs/client_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Client, id=pk)

class CategoryCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Category
    form_class = CategoryForm

    def get_initial(self):
        client = get_object_or_404(Client, pk=self.kwargs.get('pk'))
        user = self.request.user
        return {
            'client':client,
            'user':user,
        }

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Category
    fields = ['name',]
    template_name_suffix = '_update_form'

class CategoryDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Category

    def get_success_url(self):
        return reverse_lazy('client_detail', args = (self.object.client.id,))


#Documents
class CategoryDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    template_name = 'docs/category_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Category, id=pk)

class DocumentCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Document
    form_class = DocumentForm

    def get_initial(self):
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        client = get_object_or_404(Client, id=self.kwargs.get('client_id'))
        user = self.request.user
        return {
            'client':client,
            'category':category,
            'user':user,
        }

class DocumentUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Document
    form_class = DocumentForm
    template_name_suffix = '_update_form'

class DocumentDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Document

    def get_success_url(self):
        return reverse_lazy('category_detail', args = (self.object.client.id, self.object.category.id,))


#Steps
class DocumentDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    template_name = 'docs/document_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Document, id=pk)

class StepCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    model = Step
    form_class = StepForm

    def get_initial(self):
        document = get_object_or_404(Document, pk=self.kwargs.get('pk'))
        category = get_object_or_404(Category, id=self.kwargs.get('category_id'))
        client = get_object_or_404(Client, id=self.kwargs.get('client_id'))
        return {
            'document':document,
            'category':category,
            'client':client,
        }

class StepUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    model = Step
    fields = ['step_num', 'text', 'note', 'image']
    template_name_suffix = '_update_form'

class StepDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login'
    model = Step

    def get_success_url(self):
        return reverse_lazy('document_detail', args = (self.object.document.client.id, self.object.document.category.id, self.object.document.id,))


#Generate pdf
class Pdf(DetailView):
    template_name = 'pdf.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        document = get_object_or_404(Document, id=pk)
        params = {
            'document':document
        }
        return Render.render('pdf.html', params)
