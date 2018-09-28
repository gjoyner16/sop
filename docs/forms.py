from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'icon', 'user')
        widgets = {
            'user': forms.HiddenInput(),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('client', 'name', 'user')
        widgets = {
            'client': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

class DocumentForm(forms.ModelForm):
    APPLICATION=(
        ('JDA', 'JDA'),
        ('HighJump', 'HighJump'),
        ('SAP WMS', 'SAP WMS'),
        ('Other', 'Other'),
    )

    TYPE=(
        ('GUI', 'GUI'),
        ('Web UI', 'Web UI'),
        ('RF', 'RF'),
        ('Other', 'Other'),
    )

    application = forms.ChoiceField(choices=APPLICATION)
    type = forms.ChoiceField(choices=TYPE)

    class Meta:
        model = Document
        fields = ('name', 'description', 'application', 'version', 'type', 'client', 'category', 'user')
        widgets = {
            'client': forms.HiddenInput(),
            'category': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ('document', 'step_num', 'text', 'note', 'image')
        widgets = {
            'document': forms.HiddenInput(),
        }
