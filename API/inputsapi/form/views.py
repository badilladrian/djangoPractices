from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

# Create your views(CONTROLLERS) here. 

def forms_list(request): 
    MAX_OBJECTS = 20 
    forms = Form.objects.all()[:MAX_OBJECTS] 

    data = {"results": list(forms.values("form_text", 
    "created_by__username", "date, →"))} 
    
    return JsonResponse(data)

def forms_detail(request, pk): 
    form = get_object_or_404(Form, pk=pk) 

    data = {"results": { "form_text": form.form_text, 
    "created_by": form.created_by.username, 
    "Date": form.date }} 
    
    return JsonResponse(data)



