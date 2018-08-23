from django.contrib import admin
from .models import ClientFolder
from .models import CategoryFolder
from .models import Document
from .models import Step

# Register your models here.
admin.site.register(ClientFolder)
admin.site.register(CategoryFolder)
admin.site.register(Document)
admin.site.register(Step)
